from lazy.utils import input, print, int
from lazy.effect import lazy, composer
from lazy.ef_app import EfApp


@composer
def sum(a, b):
    if a.left != None and b.left != None:
        return 0
    return a.left + b.left

@EfApp
def app():
    number_a = (input("input number 1 : ") << int).attempt()
    number_b = (input("input number 2 : ") << int).attempt()
    app_effect = sum(number_a, number_b) << print
    return app_effect
