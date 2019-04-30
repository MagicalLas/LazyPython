from lazy.ef_app import EfApp
from lazy.effect import composer, lazy
from lazy.either import Left, Right
from lazy.utils import input, int, print
from lazy.typematcher import Defualt, TypeMatcher, _type, chain


@composer
def sum(a, b):
    return a + b


@EfApp
def app():
    mather = TypeMatcher(
        _type(Left) < - chain(lambda x: x.left),
        _type(Right) < - chain(lambda x: 0),
    )
    number_a = (input("input number 1 : ") << int).attempt() & mather
    number_b = (input("input number 2 : ") << int).attempt() & mather
    app_effect = sum(number_a, number_b) << print
    return app_effect
