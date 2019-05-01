# LazyPython

[![codecov](https://codecov.io/gh/Las-Wonho/LazyPython/branch/master/graph/badge.svg)](https://codecov.io/gh/Las-Wonho/LazyPython)
[![CircleCI](https://circleci.com/gh/Las-Wonho/LazyPython/tree/master.svg?style=svg)](https://circleci.com/gh/Las-Wonho/LazyPython/tree/master)

Library for Pure Functional Programming

## Useage

```python
from lazy.effect import lazy

@lazy
def sum(a, b):
    return a + b

sum_effect = sum(2, 4)
sum_effect.execute # 2 + 4
```

## Test

```bash

pytest --cov-report term-missing --cov=lazy
```
