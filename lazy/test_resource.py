from .effect import pure, lazy
from .utils import input
from .resource import Resource
from .either import Left, Right

def test_resource(monkeypatch):
    monkeypatch.setattr('lazy.utils._input', lambda x: "Lazy")

    resource_effect = input("Get Resource")
    resource = Resource.make(resource_effect)(lazy(lambda x: x))
    resource = resource.use(lambda x:x+"~!").flatMap(lazy(lambda x: x)).map(lambda x: x)
    assert resource.execute == "Lazy~!"

def test_resource_attmept(monkeypatch):
    monkeypatch.setattr('lazy.utils._input', lambda x: "Lazy")

    resource_effect = input("Get Resource")
    resource = Resource.make(resource_effect)(lazy(lambda x: x))
    resource = resource.use(lambda x:x+"~!").attempt
    assert isinstance(resource.execute, Left)

    resource_effect = input("Get Resource")
    resource = Resource.make(resource_effect)(lazy(lambda x: x))
    resource = resource.use(lambda x:x[100]).attempt
    assert isinstance(resource.execute, Right)