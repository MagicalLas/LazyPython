from .lazy import _, F


def test_underscore_calculate():
    f = _
    assert f(4) == 4

    f = _ + 2
    assert f(4) == 6

    f = 4 + _
    assert f(1) == 5

    f = 6 + _ + 2
    assert f(1) == 9

    f = 2 * (6 + _ * 2)
    assert f(4) == 28

    f = _ + _
    assert f(4) == 8

    f = 3 * _ + _ * 2
    assert f(4) == 20

    assert list(map(_ * 2, [1, 2, 3])) == [2, 4, 6]


def test_underscore_with_functions():
    def add(x, y):
        return x + y

    f = F(str)(_ + 3)
    assert f(2) == "5"

    f = F(add)(_, 3)
    assert f(2) == 5

    f = F(add)(x=_, y=3)
    assert f(2) == 5

    f = F(add)(_, y=3)
    assert f(2) == 5

    assert list(map(F(str)(_ * 2), [1, 2, 3])) == ['2', '4', '6']
    assert list(map(F(str)(_ * _), [1, 2, 3])) == ['1', '4', '9']
    assert list(map(F(add)(1, _ * 2), [1, 2, 3])) == [3, 5, 7]
    assert list(map(F(add)(_ * 2, 4), [1, 2, 3])) == [6, 8, 10]
    assert list(map(F(add)(_ * 3, _ + 2), [1, 2, 3])) == [6, 10, 14]
