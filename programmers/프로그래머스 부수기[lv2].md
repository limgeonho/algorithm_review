## 프로그래머스 부수기[Lv 2]



## 1. Level 2

- 문자열.title(), 문자열.capitalize()

  => title()는 단어마다 전부 대문자로 바꿈(단, 첫 글자가 문자가 아니면 두 번째 문자로 바뀜)

  => capitalize()는 전체 문자열 중 첫 글자만 대문자로 바꿈



- 빠르게 값을 찾기 위해서는 반드시 메모이제이션 활용하기

  ```python
  def fibo(n):
      answer = 0
      arr = [0] * 100001
      arr[1] = 1
      arr[2] = 1
      for i in range(3, n+1):
          arr[i] = arr[i-1] + arr[i-2]
      return answer
  ```



- 행렬의 곱셈(암기)

  ```python
  arr1 = [...]
  arr2 = [...]
  
  row = len(arr1)
  col = len(arr2[0])
  
  answer = [[0] * col for _ in range(row)]
  
  for i in range(row):
      for j in range(col):
          for k in range(len(arr1[0])):
              answer[i][j] += arr1[i][k] * arr2[k][j]
  return answer
  ```



- 투포인터 알고리즘

  ```python
  n = 5
  target = 5
  data = [1, 2, 3, 4, 5]
  
  cnt = 0
  interval = 0
  end = 0
  
  for start in range(n):
      while interval < target and end < n:
          interval += data[end]
          end += 1
      if interval == target:
          cnt += 1
      interval -= data[start]
  ```



- 구간합(Prefix Sum)

  ```python
  # 데이터의 개수
  n = 5
  data = [10, 20, 30, 40, 50]
  
  summary = 0
  prefix_sum = [0]
  
  for x in data:
      summary += x
      prefix_sum.append(summary)
  
  left = 3
  right = 4
  
  # 핵심 prefix_sum[R] - prefix_sum[L-1]
  print(prefix_sum[right] - prefix_sum[left-1])
  ```



- 해당 문제가 왜 DP문제인지 알아내는 과정이 중요함

  

- 자료구조 stack, queue, deque 항상 활용고민하기



- 리스트에서 원하는 요소의 index 찾는 방법

  => list.index(value)

  => 만약에 존재하지 않는 다면 error 발생함



- 원하는 목적지로 이동하는 문제의 경우 

  => 목적지에서 출발지로 거꾸로 가는 경우를 생각하기



- 2차원 리스트를 1차원 리스트로 만들기(row major order)

  ```python
  for i in range(n*n):
      x = i // n	# 행 번호
      y = i % n	# 열 번호
  ```



- 특정 리스트 형태 만들기

  ```python
  arr = [[1, 2, 3]
         [2, 2, 3]
         [3, 3, 3]]
  
  n = 3
  answer = []
  for i in range(n*n):
      x = i // n
      y = i % n
      answer.append(max(x, y) +1)
  
  return answer
  ```



- 문자열의 특정 문자를 원하는 문자로 바꾸는 방법

  => replace함수 

  => s.replace('0', '1')

  => s라는 문자열안에 있는 모든 0을 1로 바꾼다



- 중복순열 구하기 + product

  ```python
  # 기존의 중복순열 구하는 방법
  arr = [1, 2, 3, 4, 5]
  res = [0] * n
  
  def perm_with(L):
      if L == n:
          print(res)
          return
      for i in range(len(arr)):
          res[L] = arr[i]
   
  perm_with(0)
  
  #############################################################
  # itertools product 사용
  from itertools import product
  list(product(arr, repeat = n))
  # 장점은 구현이 간단하고 중복순열의 인자의 개수를 간편하게 조절할 수 있다.
  ```

  



## 2. Level 2 에서 다시 풀어볼 만한 문제

- 땅따먹기 - DP... => 브루트 포스인줄 알았지만.. 아님
- 가장 큰 정사각형 찾기 - DP
- 모음사전 - 중복순열
