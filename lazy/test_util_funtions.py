from .effect import Effect
from .utils import print, _print, input, _input, abs, _abs, all, _all, any, _any, bool, _bool, chr, _chr, divmod, _divmod, int, _int, str, _str


def test_lazy_print():
    print_effect = print('will not printed text')
    assert isinstance(print_effect, Effect)
    assert not isinstance(_print, Effect)
    assert print_effect.execute is None


def test_lazy_input(monkeypatch):
    monkeypatch.setattr('lazy.utils._input', lambda x: "Lazy")
    input_effect = input('will not printed text')
    assert isinstance(input_effect, Effect)
    assert not isinstance(_input, Effect)
    assert input_effect.execute == "Lazy"


def test_lazy_abs():
    abs_effect = abs(-3)
    assert isinstance(abs_effect, Effect)
    assert abs_effect.execute == 3

    not_abs_effect = _abs(-3)
    assert not isinstance(not_abs_effect, Effect)
    assert not_abs_effect == 3


def test_lazy_all():
    all_effect = all([True, False, False])
    assert isinstance(all_effect, Effect)
    assert not all_effect.execute

    not_all_effect = _all([True, False, False])
    assert not isinstance(not_all_effect, Effect)
    assert not not_all_effect


def test_lazy_any():
    any_effect = any([False, True, False])
    assert isinstance(any_effect, Effect)
    assert any_effect.execute == True

    not_any_effect = _any([False, True, False])
    assert not isinstance(not_any_effect, Effect)
    assert not_any_effect == True


def test_lazy_bool():
    bool_effect = bool(0)
    assert isinstance(bool_effect, Effect)
    assert not bool_effect.execute

    not_bool_effect = _bool(0)
    assert not isinstance(not_bool_effect, Effect)
    assert not not_bool_effect


def test_lazy_chr():
    chr_effect = chr(76)
    assert isinstance(chr_effect, Effect)
    assert chr_effect.execute == 'L'

    not_chr_effect = _chr(76)
    assert not isinstance(not_chr_effect, Effect)
    assert not_chr_effect == 'L'


def test_lazy_divmod():
    div_mod_effect = divmod(5, 2)
    assert isinstance(div_mod_effect, Effect)
    assert div_mod_effect.execute == (2, 1)

    not_div_mod_effect = _divmod(5, 2)
    assert not isinstance(not_div_mod_effect, Effect)
    assert not_div_mod_effect == (2, 1)


def test_lazy_int():
    int_effect = int('5')
    assert isinstance(int_effect, Effect)
    assert int_effect.execute == 5

    not_int_effect = _int('5')
    assert not isinstance(not_int_effect, Effect)
    assert not_int_effect == 5


def test_lazy_str():
    str_effect = str(20)
    assert isinstance(str_effect, Effect)
    assert str_effect.execute == "20"

    not_str_effect = _str(20)
    assert not isinstance(not_str_effect, Effect)
    assert not_str_effect == "20"
