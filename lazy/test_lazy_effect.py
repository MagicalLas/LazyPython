from .effect import lazy, Effect


@lazy
def sum(a, b):
    return a + b


def mul(a):
    @lazy
    def lazy_mul(b):
        return a * b
    return lazy_mul


def test_lazy_sum():
    sum_effect = sum(1, 2)

    assert isinstance(sum_effect, Effect)

    assert sum_effect.excute() == 1 + 2
    assert not sum_effect.excute() == 1 + 3


def test_lazy_maps():
    sum_effect = sum(1, 2)
    result = sum_effect\
        .map(lambda x: x + 1)\
        .map(lambda x: x + 2)\
        .map(lambda x: x + 3)\
        .excute()
    assert result == 1 + 2 + 1 + 2 + 3


def test_lazy_one_multiplex():
    multiplexer = mul(2)
    sum_effect = sum(1, 2)
    chain_effect = sum_effect\
        .flatMap(multiplexer)\
        .flatMap(multiplexer)\
        & (lambda x: x - 4)

    assert chain_effect.excute() == (3 * 2 * 2) - 4
