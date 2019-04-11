from lazy.lazy import print
from lazy.effect_app import EfApp


@EfApp
def app():
    helloworld_app = print("hello world~!")
    return helloworld_app
