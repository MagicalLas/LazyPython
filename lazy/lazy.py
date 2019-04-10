_print = print


class Effect(object):
    def __init__(self, f, a, w):
        self.f = f
        self.a = a
        self.w = w

    def excute(self):
        return self.f(*self.a, **self.w)

    def flatMap(self, f):
        e = Effect(self.f, self.a, self.w)
        return ChainEffect([e, f])

    def map(self, f):
        @lazy
        def dummy():
            return f(self.excute())
        return dummy()

    def __lshift__(self, f):
        return self.flatMap(f)


class ChainEffect(object):
    def __init__(self, effect_list):
        self.effects = effect_list

    def map(self, f):
        @lazy
        def dummy():
            return f(self.excute())
        return dummy()

    def flatMap(self, f):
        self.effects.append(f)
        return self

    def __lshift__(self, f):
        return self.flatMap(f)

    def excute(self):
        value = self.effects[0].excute()
        for effect in self.effects[1:]:
            value = effect(value).excute()
        return value


def lazy(function):
    def f(*arg, **kwargs):
        return Effect(function, arg, kwargs)
    return f


@lazy
def print(*arg, **kwargs):
    _print(*arg, **kwargs)
