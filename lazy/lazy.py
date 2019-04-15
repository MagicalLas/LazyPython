from .either import Either

_print = print
_input = input


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
                return Either.right(self.excute())
            except Exception as e:
                return Either.left(e)
        return dummy()

    def __lshift__(self, f):
        return self.flatMap(f)

    def __and__(self, f):
        return self.map(f)


def lazy(function):
    def f(*arg, **kwargs):
        return Effect(function, arg, kwargs)
    return f


@lazy
def print(*arg, **kwargs):
    return _print(*arg, **kwargs)


@lazy
def input(*arg, **kwargs):
    return _input(*arg, **kwargs)
