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

[![codecov](https://codecov.io/gh/Las-Wonho/LazyPython/branch/master/graph/badge.svg)](https://codecov.io/gh/Las-Wonho/LazyPython)

```bash

pytest --cov-report term-missing --cov=lazy
```
