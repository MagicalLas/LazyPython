# Resource

리소스를 가져오고 해재하는것 또한 Effect입니다. 순수함수형 프로그래밍을 하기위하여 이를 제어하는 Resource라는 타입을 제공해줍니다.

## 생성

Reource를 생성하는 방법은 리소스를 할당하고 해제하는 함수를 등록하는것으로 가능합니다. make라는 메소드를 사용하여 Resource생성을 시작할 수 있습니다. Resource를 생성하는 과정을 크게 2가지로 나눠집니다. make메소드로 resource를 반환하는 effect를 매개변수로 넘겨줍니다. 그리고 resource를 받아 해제해주는 함수를 넘겨줍니다.

```python
from lazy.utils import input, print

@lazy
def closer(resource):
    print(resource)

resource_effect = input("Get Resource")

Reource.make(resource_effect)(closer)
```

## Chainning

함수들을 Chain할 때 가장 먼저 use를 써야합니다. use의 형식은 function[resource => F]입니다. 그 뒤로 map, flatMap과 같은 메서드를 사용하여 Chain을 진행할 수 있습니다. map의 형식은 function[F => G]이며 flatMap의 형식은 function[F => Effect[G]]입니다.

```python
resource_effect = input("Your Name : ")
resource = Reource.make(resource_effect)(closer)
resource = resource.use(lmabda x:x+"~!").map(lmabda x:"Hello "+x).flatMap(print)
```

## 해제과정

Resource를 해제하는 시기는 excute메소드가 실행된 시점입니다. 이 메소드에서 use나 map, flatMap으로 엮은 함수체인이 실행되게됩니다. 이 체인이 끝난후 리소스는 넘겨준 함수에 의하여 해제됩니다.
