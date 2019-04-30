# TypeMatching

TypeMatcher은 타입에 따라 여러 동작을 실행하는 함수를 뜻합니다.

## Usage

`_type`키워드로 매개변수의 Type을 감싸줍니다. 그리고 `<-`키워드를 통하여 함수를 타입에 종속시킬 수 있습니다. 이 때 함수는 `chain`이라는 키워드로 감싸주어야합니다. 람다 여러개를 `chain`으로 합칠수도 있습니다. Default라는 Type은 모든 타입에 관하여 유효합니다. 심지어 Nonetype도 가능합니다.

```python
mather = TypeMatcher(
    _type(int) < - chain(lambda x: x.left),
    _type(str) < - chain(lambda x: 0),
    _type(Defualt) < - chain(lambda x: print("else"),
                             lambda _: 0),
)
```

실제 Effect와 합성할 때 `&`이나 `map`이라는 키워드를 사용하여 간단하게 합칠 수 있습니다. 그 이유는 TypeMatcher는 callable한 함수시기 때문에 함수와 동일한 취급을 받습니다.

## Use with Either

Either와 함께 사용하면 에러처리를 쉽게 할 수 있습니다. Either의 타입은 Left, Right가 있습니다. 주로 Left가 성공, Right가 실패하였을 경우를 나타냅니다. 이러한 타입매칭으로 에러 분기를 쉽게 실행할 수 있습니다.

```python
mather = TypeMatcher(
    _type(Left) < - chain(lambda x: x.left),
    _type(Right) < - chain(lambda x: 0),
)
```
