# LazyPython

Lazy evaluation helper using effect

## Useage

```python
from lazy import lazy

@lazy
def sum(a, b):
    return a + b

sum.excute()
```

## Test

```bash
pytest test.py
```
