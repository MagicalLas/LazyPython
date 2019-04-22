from .effect import lazy

_print = print
_input = input

_int = int
_chr = chr
_bool = bool
_str = str

_abs = abs
_all = all
_any = any
_divmod = divmod


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
def chr(*arg, **kwargs):
    return _chr(*arg, **kwargs)


@lazy
def bool(*arg, **kwargs):
    return _bool(*arg, **kwargs)


@lazy
def str(*arg, **kwargs):
    return _str(*arg, **kwargs)


@lazy
def abs(*arg, **kwargs):
    return _abs(*arg, **kwargs)


@lazy
def all(*arg, **kwargs):
    return _all(*arg, **kwargs)


@lazy
def any(*arg, **kwargs):
    return _any(*arg, **kwargs)


@lazy
def divmod(*arg, **kwargs):
    return _divmod(*arg, **kwargs)
