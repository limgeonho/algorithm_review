## 프로그래머스 부수기[Lv 3]



## 1. Level 3

- defaultdict(list)에서 value값(list)을 정렬할때

  ```python
  for ticket in tickets:
      airport[ticket[0]].append(ticket[1])
  
  # value가 리스트일때 정렬하기
  for key in airport.keys():
      airport[key].sort()
  ```

  

## 2. Level 3 에서 다시 풀어볼 만한 문제

- 카카오
  - 여행경로 - 방법은 맞은 것 같은데...
