def is_callable(x):
    return hasattr(x, '__call__')


def value_function(value):
    return lambda x: value


class Underscore(object):
    def __init__(self, value):
        self.f = is_callable(value) and value or value_function(value)

    def __call__(self, *args, **kargs):
        return self.f(*args)

    def __add__(self, other):
        f = lambda x: self.f(x) + Underscore(other)(x)
        return Underscore(f)

    def __radd__(self, other):
        f = lambda x: Underscore(other)(x) + self.f(x)
        return Underscore(f)

    def __mul__(self, other):
        f = lambda x: self.f(x) * Underscore(other)(x)
        return Underscore(f)

    def __rmul__(self, other):
        f = lambda x: Underscore(other)(x) * self.f(x)
        return Underscore(f)


def F(f):
    def function(*args, **kargs):
        args = [Underscore(v) for v in args]
        kargs = {k: Underscore(v) for k, v in kargs.items()}
        return lambda x: f(
            *[arg(x) for arg in args],
            **{k: v(x) for k, v in kargs.items()}
        )

    return function


_ = Underscore(lambda x: x)
