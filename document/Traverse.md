# Traverse

Traverse는 [List[EffectT] => Effect[ListT]]인 함수입니다. 어떠한 값 T를 담고있는 Effect의 List가 있을때 `traverse`함수를 적용시키면 T를 담고있는 List의 Effect가 됩니다.

## Usage

Traverse를 사용하는 경우 이러한 List를 사용해서 여러 값을 처리할 수도 있습니다.

```python
# [EffectT, EffectT, EffectT]
effect_list = [input("input number 1 : ") << int,
               input("input number 2 : ") << int,
               input("input number 3 : ") << int]
# Effect[T, T, T]
effect_list_t = traverse(effect_list)
```

## Time Complex

`traverse`를 적용한 Effect의 값을 평가하는 시간복잡도는 N^2입니다. List에 append하는 연산을 N번 하기때문입니다. 그러나 이 함수를 실행할 당시의 시간복잡도는 N이 됩니다. List에 append하는 함수를 map으로 N번 실행하기 때문입니다.

## What Diff for Composer

`composer`와 `traverse`모두 여러 모나드를 동시에 처리해야할 때 유용합니다. 또한 두 함수 모두 다 매개변수의 수가 정해지지않은 함수에도 적용이 가능합니다. 그러나 `composer`는 문법적 설탕이지만 `traverse`는 더 유서깊은 함수입니다.
