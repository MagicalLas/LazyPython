# LazyPython

Library for Pure Functional Programming

## Useage

```python
from lazy.effect import lazy

@lazy
def sum(a, b):
    return a + b

sum_effect = sum(2, 4)
sum_effect.excute() # 2 + 4
```

## Test

```bash
cd  lazy
pytest
```
