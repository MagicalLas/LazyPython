# LazyPython

Lazy evaluation helper using effect

## Useage

```python
from lazy import lazy, input

@lazy
def sum(a, b):
    return a + b

sum(1,2).excute()

input_effect = input("Hello! Lazy World")
input_effect.excute()
```

## Test

```bash
pytest test.py
```
