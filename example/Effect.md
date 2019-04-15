# Effect

Effect는 lazy한 함수를 실행시키면 생성되는 값의 타입입니다. 이를 이용해서 순수 함수형 프로그램을 제작할 수 있습니다.

## lazy

Effect를 생성하기 위하여 lazy한 함수를 실행시켜야합니다. 데코레이터를 이용하여 lazy한 함수를 제작할 수 있습니다. lazy한 함수를 실행시키면 실제로 실행되지않고 Effect가 생성됩니다. 이 Effect는 실제 값을 계산하지않고 나중에 excute를 통하여 실행시킬 수 있습니다. 또한 lambda를 사용하여서 간단한 lazy함수를 만들 수도 있습니다.

```python
@lazy
def lazy_print(arg):
    print(arg)
lazy_print("lazy python") # Effect
lazy(lambda a,b: a+b)(2, 3) # Effect
```

## map

Effect들은 map이라는 메소드를 지원합니다. 입력 파라미터는 function(F => G)입니다. 이 함수의 입력은 그 전 함수의 결과가 입력으로 들어오게됩니다. 이 메소드를 사용하게되면 새로운 effect를 생성하게됩니다.

```python
@lazy
def sum(a,b):
    return a + b
def add4(a):
    return a + 4
sum(2,3).map(add4).excute() # (2 + 3) + 4
```

map이라는 메소드 대신에 &이라는 operator를 사용하여서 map연산을 할 수도 있습니다.

```python
result = sum(2,3) & add4
result.excute() # (2 + 3) + 4
```

## flatMap

Effect들은 flatMap이라는 메소드를 지원합니다. 입력 파라미터는 function(F => Effect[G])입니다. 이 함수의 입력은 그 전 함수의 결과가 입력으로 들어오게됩니다. 이 메소드를 사용하게되면 새로운 effect를 생성하게됩니다.

```python
@lazy
def sum(a,b):
    return a + b
@lazy
def add4(a):
    return a + 4
sum(2,3).flatMap(add4).excute() # (2 + 3) + 4
```

map이라는 메소드 대신에 <<이라는 operator를 사용하여서 flatMap연산을 할 수도 있습니다.

```python
result = sum(2,3) << add4
result.excute() # (2 + 3) + 4
```

## attempt

Effect[F] => Effect[Either[G, Err]}로 바꿔주는 특수한 메소드입니다. 지금까지 chain된 함수들중에서 에러가 발생한다면 Either의 left에 값이 있고 에러가 나지않았다면 Either의 right에 값이 존재하게됩니다. 값이 없는경우는 None이 들어있게됩니다.

## 주의사항

- <<와 &의 우선순위가 달라 오류가 날 수도 있습니다.
- function chain이 재귀적으로 실행되기때문에 너무 많은 연결은 에러를 발생시킬 수도 있습니다.
- map과 flatMap을 헷갈리지말아야합니다.
- 그 전 함수의 반환값을 신경써야합니다. 만약 여러값을 주어야하는경우 input parameter는 1개로 두고 반환값을 []이나 ()로 묶으면 해결할 수 있습니다.