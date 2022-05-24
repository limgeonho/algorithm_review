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



- DP - 정수 삼각형

  => DP문제는 작은 문제들로 나눠봐야함...

  => 작은 문제의 규칙이 큰 문제들로 확장했을 경우에도 적용된다.

  => 처음부터 전체를 한 번에 보려하면 오히려 어렵고 안보임

  => 하지만 맨 초기 단계부터 차근차근 규칙을 찾으면 보인다!!

  => 따라서, 

  => 1. 초기 모양부터 하나씩 차근차근 규칙을 살펴본다

  => 2. 초기 단계의 규칙이 다음 단계에서도 똑같이 적용되는지 확인한다

  => DP는 생각보다 어렵게 안나온다...(규칙 찾는거니까~)



- 예전부터 코딩테스트에서 자주 나오는 문제

  => 문자열이 주어지고 앞뒤 같은 문자가 나오면 압축하는 문제

  ```python
  text = 'aaaabbcccdeef'
  answer = ''
  
  text += ''
  cnt = 1
  for i in range(len(text) - 1):
      if text[i] == text[i+1]:
          cnt += 1
      else:
          answer += text[i]
          if cnt > 1:
              answer += (text[i] + str(cnt))
              cnt = 1
              
  return answer # a4b2c3de2f
  ```




- 단순하게 permutations, combinations를 사용했을 경우 시간초과로 문제가 풀리지 않느다면? - 숫자 게임

  => 다른 방법이 존재한다

  => 직접 종이에 써서 생각 ㄱㄱ

  => 정렬을 한다던지...

  => 하나씩 빼서 비교한다던지 

  => 쉽게 생각하기



- knapsack 알고리즘

  ```python
  # 물건을 무한 개 사용할 수 있는 경우
  n, limit = map(int, input().split())
  dp = [0] * (limit + 1)
  
  for i in range(n):
      weight, value = map(int, input().split())
      for j in range(limit, weight-1, -1):
          dp[j] = max(dp[j], dp[j - weight] + value)
  
  return dp[limit]
  
  # 물건을 1개 사용할 수 있는 경우
  n, limit = map(int, input().split())
  dp = [0] * (limit + 1)
  
  for i in range(n):
      weight, value = map(int, input().split())
      for j in range(weight, limit + 1):
          dp[j] = max(dp[j], dp[j - weight] + value)
        
  return dp[limit]
  ```




- 순열, 조합, 중복순열, 중복조합

  ![1](https://user-images.githubusercontent.com/73927750/167124947-7cbc4147-83df-4496-863a-47884e6f510d.png)



- imos 기법 - 카카오 - 파괴되지 않은 건물

  => 2차원 리스트를 순회하면서 특정 영역(사각형 모양)의 값을 전부 바꾸는 행위를 반복할 때

  => 직접 2차원 리스트를 순회하면서 매번 update하면 시간이 매우 많이 걸린다

  => 2차원 리스트를 전체 1번만 순회하면서도 전체를 한 번에 update할 수 있다

  => how? 

  => imos 기법!!!!(누적합)

  => imos 기법은 2차원 리스트에서 원하는 구역에 추가할 값을 해당 시작점과 끝점에만 표시를 전부 다 수행하고

  => 마지막에 최종적으로 전체 2차원 리스트를 돌면서 누적합을 구하는 방법임

  => 따라서, (시작점, 끝점) 표시만 하고 전체 2차원 리스트는 1번만 순회(행으로, 열로)하면 전체 쿼리를 실행한 결과를 알 수 있다.

  ![imos](https://user-images.githubusercontent.com/73927750/167453998-d2ba6e7f-d5ee-4725-a0bd-4748f3cf7476.png)

  ```python
  # imos 기법
  def imos(changed, skills):
      for skill in skills:
          r1 = skill[1]
          c1 = skill[2]
          r2 = skill[3]
          c2 = skill[4]
          degree = skill[5]
      
      # ======== imos ======== 
          if skill[0] == 1:
              changed[r1][c1] -= degree
              changed[r1][c2+1] += degree
              changed[r2+1][c1] += degree
              changed[r2+1][c2+1] -= degree
          else:
              changed[r1][c1] += degree
              changed[r1][c2+1] -= degree
              changed[r2+1][c1] -= degree
              changed[r2+1][c2+1] += degree
      
      # 행 sweep
      for r in range(n+1):
          for c in range(1, m+1):
              changed[r][c] += changed[r][c-1]
      
      # 열 sweep
      for c in range(m+1):
          for r in range(1, n+1):
              changed[r][c] += changed[r-1][c]
      
      # ======================
      return
  ```




- 배열 회전하기

  1. ```python
     arr = list(map(list, zip(*arr)))[::-1]
     ```
  
  2. ```python
     def rotate_matrix_by_90_degree_2(a):
     
         changed = [k[::-1] for k in zip(*a)]
     
         return changed
     ```
  
     
  
- 그리디

- 완전탐색

## 2. Level 3 에서 다시 풀어볼 만한 문제

- 여행경로 - 방법은 맞은 것 같은데...
- 야근 지수 - 힙
- 줄 서는 방법 - 라이브러리 쓰면 시간초과
- 입국 심사 - 이분탐색
- 단속 카메라 - 그리디, 정렬과 밀접한 연관..
- 정수 삼각형 - DP
  - 카카오
    - 파괴되지 않은 건물 - imos
