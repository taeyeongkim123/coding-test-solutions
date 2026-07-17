# 유용한 파이썬 기능 메모

코딩테스트 풀면서 알아두면 좋은 파이썬 기능들을 정리합니다.

## defaultdict

키가 없을 때 자동으로 기본값을 생성해주는 딕셔너리. 존재 여부를 매번 확인하지 않아도 돼서 코드가 간결해진다.

```python
from collections import defaultdict

# 빈 리스트를 기본값으로 자동 생성하는 딕셔너리
dict_list = defaultdict(list)
dict_list['사과'].append(1)  # '사과' 키가 없어도 에러 없이 빈 리스트에 추가

# 0을 기본값으로 자동 생성하는 딕셔너리
dict_int = defaultdict(int)
dict_int['개수'] += 1       # '개수' 키가 없으면 0으로 시작하여 1을 더함
```
