from .effect import traverse, pure, Effect

def test_pure():
    p = pure("Lazy")
    assert isinstance(p, Effect)
    assert p.execute == "Lazy"

def test_traverse():
    effects = [pure(5), pure(-5), pure(3), pure(0)]
    effect_t = traverse(effects)
    assert isinstance(effect_t, Effect)
    assert effect_t.execute == [5, -5, 3, 0]