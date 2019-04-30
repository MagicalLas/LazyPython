from .either import Either, Left, Right

def test_Either():
    lEither = Either.left(4)
    rEither = Either.right("Lazy")
    assert isinstance(lEither, Left)
    assert isinstance(rEither, Right)
    assert lEither.left == 4
    assert rEither.right == "Lazy"