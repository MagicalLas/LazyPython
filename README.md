# LazyPython

Lazy evaluation helper using effect

## Useage

```python
from lazy import lazy, input

@lazy
def sum(a, b):
    return a + b

sum_effect = sum(1,2)
sum_effect.excute() # 1 + 2

input_effect = input("Hello! Lazy World")
input_effect.excute() # will printing "Hello! Lazy World"
```

## Test

```bash
pytest test.py
```
