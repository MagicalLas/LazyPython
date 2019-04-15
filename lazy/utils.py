from .lazy import lazy

_print = print
_input = input


@lazy
def print(*arg, **kwargs):
    return _print(*arg, **kwargs)


@lazy
def input(*arg, **kwargs):
    return _input(*arg, **kwargs)
