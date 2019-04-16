from lazy.utils import print
from lazy.ef_app import EfApp


@EfApp
def app():
    helloworld_app = print("hello world~!")
    return helloworld_app
