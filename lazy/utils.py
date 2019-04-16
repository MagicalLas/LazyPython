from .lazy import lazy

_print = print
_input = input

_int = int
_string = string


@lazy
def print(*arg, **kwargs):
    return _print(*arg, **kwargs)


@lazy
def input(*arg, **kwargs):
    return _input(*arg, **kwargs)

@lazy
def int(*arg, **kwargs):
    return _int(*arg, **kwargs)

@lazy
def string(*arg, **kwargs):
    return _string(*arg, **kwargs)