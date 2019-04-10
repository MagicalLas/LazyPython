from lazy import lazy, ChainEffect, Effect, print

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


def test_effect_chain():
    sum_effect = sum(1, 2)
    print_effect = sum_effect.map(print)

    assert isinstance(print_effect, ChainEffect)


def test_lazy_one_multiplex():
    multiplexer = mul(2)
    sum_effect = sum(1, 2)

    result_effect = sum_effect\
        .map(multiplexer)

    assert isinstance(result_effect, ChainEffect)
    assert result_effect.excute() == 3 * 2


def test_lazy_multiplex():
    multiplexer = mul(2)
    sum_effect = sum(1, 2)

    result_effect = sum_effect\
        .map(multiplexer)\
        .map(multiplexer)\
        .map(multiplexer)

    assert isinstance(result_effect, ChainEffect)
    assert result_effect.excute() == 3 * 2 * 2 * 2
