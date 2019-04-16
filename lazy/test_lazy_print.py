from .effect import Effect
from .utils import print

def test_lazy_print():
    print_effect = print('will not printed text')
    assert isinstance(print_effect, Effect)
