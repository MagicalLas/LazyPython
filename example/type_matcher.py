from lazy.utils import input
from lazy.ef_app import EfApp
from lazy.typematcher import Defualt, TypeMatcher, _type, chain


@EfApp
def app():
    number_a = (input("input number 1 : ") & int)
    string_a = input("input name : ")
    mather = TypeMatcher(
        _type(int) <- chain(lambda x: print("Your Number is %d" % x)),
        _type(str) <- chain(lambda x: print("Your Name is %s" % x)),
        _type(Defualt) <- chain(lambda x: print("NOPE~!"))
    )
    return string_a & mather
