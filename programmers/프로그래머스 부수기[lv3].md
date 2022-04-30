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



- 리스트에서 매번 최대값이나 최소값을 뽑아내서 이용해야하는 경우

  => 1번 방법 : 매번 리스트의 min(), max() 연산을 한다

  => 2번 방법 : 리스트를 heapify(list) 통해 heap으로 만들고 min heap, max heap으로 바꿔서 연산한다

  => 당연히 2번 방법을 사용해야 시간이 엄청나게 줄어든다!!!

  

- Level 3 부터는 DP문제들이 나오기 시작함!

  => 아직까지는 기본적인 피보나치 수열문제



- 이분탐색 문제는 해당 문제가 이분탐색을 활용해야하는지 파악하는게 중요함

  => 이분 탐색이라는 것을 파악했다면 

  => 시작점, 끝점을 파악해야함

  => 시작점 : 가장 작은 값(대부분 1)

  => 끝점 :  해당 문제에서 발생가능한 최악의 경우

  => 이후에 중간값을 계산해가며 해당 조건에 부합하는지 파악 후 최적해 도출!!



- dictionary sorting하기

  => list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

  => dict.items() 부분이 핵심



- sort의 lambda함수에서 하나는 오름차순, 하나는 내림차순으로 하려면

  => key 값 설정에서 여러개의 기준을 준다

  => tmp = sorted(tmp, key=lambda x: (x[0], -x[1]))

  => [0] 은 오름차순 + [1] 은 내림차순



- 크루스칼 알고리즘

  => MST를 구하는 알고리즘

  ```python
  # 크루스칼 알고리즘
  def find_parent(parent, x):
      if parent[x] != x:
          parent[x] = find_parent(parent, parent[x])
      return parent[x]
  
  def union_parent(parent, a, b):
      a = find_parent(parent, a)
      b = find_parent(parent, b)
      if a < b:
          parent[b] = a
      else:
          parent[a] = b   
  
  parent = [0] * n
  for i in range(n):
      parent[i] = i
  answer = 0
      
  for cost in costs:
      a, b, co = cost
      if find_parent(parent, a) != find_parent(parent, b):
          union_parent(parent, a, b)
          answer += co
  
  return answer
  
  ```



- 그리디 알고리즘

  => 그리디는 정렬과 밀접한 연관이 있기 때문에

  => 그리디라고 판단되면 다양한 조건으로 정렬해보자!!

  => 문제에서 항상 최소~ 최대~ 몇 개를 구하시오 => 이런식으로 문제가 나옴



- ㅇㄴㅁ

## 2. Level 3 에서 다시 풀어볼 만한 문제

- 여행경로 - 방법은 맞은 것 같은데...
- 야근 지수 - 힙
- 줄 서는 방법 - 라이브러리 쓰면 시간초과
- 입국 심사 - 이분탐색
- 단속 카메라 - 그리디, 정렬과 밀접한 연관..
