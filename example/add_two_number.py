from lazy.utils import input, print, int
from lazy.effect import lazy
from lazy.ef_app import EfApp


@lazy
def sum(a, b):
    if a.right or b.right:
        return 0
    return a.left + b.left

@EfApp
def app():
    number_a = (input("input number 1 : ") << int).attempt()
    number_b = (input("input number 2 : ") << int).attempt()
    app_effect = sum(number_a.excute(), number_b.excute()) << print
    return app_effect
