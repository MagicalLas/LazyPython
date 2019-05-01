from .ef_app import EfApp
from .effect import pure

def test_EfApp():
    assert EfApp(lambda: pure(5)) == pure(5).execute