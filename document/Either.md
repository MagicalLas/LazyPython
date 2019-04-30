# Either

Either는 둘중에 1개만 존재하는 상황에서 사용할 수 있는 타입입니다. left와 right값이 있습니다. Either는 Left, Right라는 타입의 Either인스턴스를 생성할 수 있습니다. 이러한 타입은 Type Matcher를 통하여 더욱 효과적인 처리가 가능합니다.

```python
lEither = Either.left(4) # Left[4]
rEither = Either.right(2) # Right[2]
lEither.left # 4
rEither.right # 2
```

## Notice

Either는 어디에도 값을 담을 수 있지만 주로 Left에 실제 값, Right에 에러값을 담아 오류를 처리하는데 사용하기도 합니다. 실제로 Effect의 attempt를 사용하면 에러 발생 유무에 따라 Left, Right를 생성합니다.
