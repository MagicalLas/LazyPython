from .either import Either
from functools import reduce


class Effect(object):
    def __init__(self, f, a, w):
        self.f = f
        self.a = a
        self.w = w

    def excute(self):
        return self.f(*self.a, **self.w)

    def flatMap(self, f):
        @lazy
        def dummy(_F):
            return _F(self.excute()).excute()
        return dummy(f)

    def map(self, f):
        @lazy
        def dummy(_F):
            return _F(self.excute())
        return dummy(f)

    def attempt(self):
        @lazy
        def dummy():
            try:
                return Either.left(self.excute())
            except Exception as e:
                return Either.right(e)
        return dummy()

    def __lshift__(self, f):
        return self.flatMap(f)

    def __and__(self, f):
        return self.map(f)


def lazy(function):
    def f(*arg, **kwargs):
        return Effect(function, arg, kwargs)
    return f


def composer(function):
    def f(*arg, **kwargs):
        arg = [i.excute() for i in arg]
        return Effect(function, arg, kwargs)
    return f


def pure(F):
    @lazy
    def dummy(f):
        return f
    return dummy(F)


def traverse(effects):
    @composer
    def append(acc, a):
        acc.append(a)
        return acc
    return reduce(append, effects, pure([]))
