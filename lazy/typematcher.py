class _type(object):
    def __init__(self, type):
        self.type = type

    def __lt__(self, function):
        self.f = function
        return self

    def available(self, type):
        if self.type == Defualt:
            return True
        return self.type == type


class Defualt(object):
    pass


class TypeMatcher(object):
    def __init__(self, *a):
        self.matchers = a

    def __call__(self, x):
        t = type(x)
        for matcher in self.matchers:
            if matcher.available(t):
                return matcher.f(x)
        return x


class _Func1(object):
    def __init__(self, function):
        self.f = function

    def __neg__(self):
        return self

    def __call__(self, x):
        return self.f(x)


def chain(*funcs):
    def F(x):
        for f in funcs:
            x = f(x)
        return x
    return _Func1(F)
