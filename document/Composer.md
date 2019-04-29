# Composer

composer는 efffect.py에 있는 Decorator입니다. 여러 Effect를 인자로 받는 함수를 만들때 편리합니다. 여러 Effect의 결과가 필요한 경우 이 composer로 합성할 수 있습니다. composer는 새로운 Effect를 생성해줍니다. 따라서 composer함수는 map/flatMap이 불가능합니다.

```python
@composer
def sum(a, b):
    return a + b
```
