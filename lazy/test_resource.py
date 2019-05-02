from .effect import pure, lazy
from .utils import input
from .resource import Resource

def test_resource(monkeypatch):
    monkeypatch.setattr('lazy.utils._input', lambda x: "Lazy")

    resource_effect = input("Get Resource")
    resource = Resource.make(resource_effect)(lazy(lambda x: x))
    resource = resource.use(lambda x:x+"~!").map(lambda x:"Hello "+x).flatMap(lazy(lambda x: x))
    assert resource.execute == "Hello Lazy~!"