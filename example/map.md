# map

Effect들은 map이라는 메소드를 지원합니다.

```python
@lazy
def sum(a,b):
    return a + b

@lazy
def add4(a):
    return a + 4
sum(2,3).map(add4).excute() # (2 + 3) + 4
```

map이라는 메소드 대신에 <<이라는 operator를 사용하여서 map연산을 할 수도 있습니다.

```python
result = sum(2,3) << add4
result.excute() # (2 + 3) + 4
```
