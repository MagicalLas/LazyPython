from .utils import input, print, _print
from .effect import pure
from .typematcher import Defualt, TypeMatcher, _type, chain, _Func1


def test_type_matching(monkeypatch):
    number_a = input("input number 1 : ") & int
    string_a = input("input name : ")
    mather = TypeMatcher(
        _type(int) < - chain(lambda x: False),
        _type(str) < - chain(lambda x: True),
        _type(Defualt) < - chain(lambda x: None)
    )
    effectA = number_a & mather
    effectB = string_a & mather

    monkeypatch.setattr('lazy.utils._input', lambda x: "90")
    assert effectA.execute is False

    monkeypatch.setattr('lazy.utils._input', lambda x: "LazyPython")
    assert effectB.execute is True
    assert mather(4) is False


def test_type_miss_matching(monkeypatch):  # miss match
    string_a = input("input name : ")
    mather = TypeMatcher(
        _type(int) < - chain(lambda x: False),
    )
    effect = string_a & mather
    monkeypatch.setattr('lazy.utils._input', lambda x: "Lazy")
    assert effect.execute == "Lazy"


def test_type_default():  # default match
    mather = TypeMatcher(
        _type(Defualt) < - chain(lambda x: "Lazy"),
    )
    effect = pure(None) & mather
    assert effect.execute == "Lazy"


def test_type():
    lazy = Defualt()
    assert isinstance(lazy, Defualt)

    t = _type(int)
    assert isinstance(t, _type)
    assert t.available(int) == True

    f = _Func1(lambda x: x + 3)
    assert f(2) == 5
    assert (-f)(2) == 5

    c = chain(lambda x: x + 3, lambda x: x - 2)
    assert c(1) == 1 + 3 - 2
