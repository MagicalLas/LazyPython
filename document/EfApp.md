# EfApp

실제로 함수형 프로그래밍을 하기위하여 excute메서드를 사용하지말아야합니다. 이러한 프로그램의 시작점이 되는 곳이 EfApp입니다. 데코레이터를 사용하여 시작점을 정의할 수 있고 Effect를 반환값으로 가져야합니다. 따라서 실제로 여러분이 작성하는 코드에서는 실제로 실행하는 곳이 존재하지않습니다. EfApp은 프로그램마다 1개만 있어야합니다. 또한 lambda를 사용한 정의보다는 데코레이터를 사용하는것을 권장합니다.

이 구조는 scala의 라이브러리인 cats IOApp에서 영감을 받아 제작하였습니다.

```python
@EfApp
def app():
    effect = lazy_input << application
    return effect
```
