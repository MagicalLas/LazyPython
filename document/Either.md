# Either

Either는 둘중에 1개만 존재하는 상황에서 사용할 수 있는 타입입니다. left와 right값이 있습니다.

```python
lEither = Either.left(4) # Either[4, None]
rEither = Either.right(2) # Either[None, 2]
lEither.left # 4
rEither.right # 2
```
