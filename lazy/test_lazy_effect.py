from .effect import lazy, Effect, pure
from .typematcher import _type, TypeMatcher, chain
from .either import Left, Right


def test_lazy_sum():
    mather = TypeMatcher(
        _type(Left) < - chain(lambda x: True),
        _type(Right) < - chain(lambda x: False),
    )

    effect = pure(4)
    effect = effect << lazy(lambda x: x / 0)
    effect = effect.attempt
    assert (effect & mather).execute is False
