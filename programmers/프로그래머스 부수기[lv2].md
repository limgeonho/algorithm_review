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



- 자료구조 stack, queue, deque 항상 활용고민하기





## 2. Level 2 에서 다시 풀어볼 만한 문제

- 

