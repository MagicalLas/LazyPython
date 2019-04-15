from .effect import Effect


def test_lazy_print():
    from .lazy import print
    print_effect = print('will not printed text')
    assert isinstance(print_effect, Effect)


def test_normal_print():
    print_effect = print('will print text')
    assert not isinstance(print_effect, Effect)
