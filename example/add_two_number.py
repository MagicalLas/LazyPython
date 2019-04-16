from lazy.utils import input, print, int
from lazy.effect import lazy
from lazy.ef_app import EfApp


@lazy
def sum(a, b):
    return a + b

@EfApp
def app():
    number_a = input("input number 1 : ") << int
    number_b = input("input number 2 : ") << int
    app_effect = sum(number_a.excute(), number_b.excute()) << print
    return app_effect
