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
          perm_with(L+1)
   
  perm_with(0)
  
  #############################################################
  # itertools product 사용
  from itertools import product
  list(product(arr, repeat = n))
  # 장점은 구현이 간단하고 중복순열의 인자의 개수를 간편하게 조절할 수 있다.
  ```



- union-find

  ```python
  parent = [0] * (n+1)
  for i in range(1, n+1):
      parent[i] = i
  
  def find_parent(parent, x):
      if parent[x] != x:
          parent[x] = find_parent(parent, parent[x])
      return parent[x]
  
  def union(parent, a, b):
      a = find_parent(parent, a)
      b = find_parent(parent, b)
      if a < b:
          parent[b] = a
      else:
          parent[a] = b
  ```



- bfs 탐색의 기본형태

  ```python
  from collections import deque
  
  def bfs(board, visited, start):
      q = deque()
      q.append(start)
      visited[start] = True
      while q:
          now = q.popleft()
          for nxt in board[now]:
              if not visited[nxt]:
                  q.append(nxt)
                  visited[nxt] = True
                  # 추가 연산
                  
  bfs(board, visited, start)
  ```



- pop(0) 보다 popleft()가 압도적으로 시간이 빠르다



- 탐욕법

  => ~~~를 최소로~

  =>  정렬과 밀접한 연관

  => 해당문제가 탐욕법 문제라면 출제자가 문제를 낼때 최적해가 나올 수 있도록 이미 설계해 놓은 것임

  => 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다



- 소수점 자르는 방법(f-string에서 소수점 관리하기)

  => print(f"{number:.nf}") 

  => 로 number의 소수점 n+1번째 자릿수에서 반올림해서 소수점 n번째 자릿수까지 출력함으로써 소수점을 관리할 수 있다.

  ```python
  print(f"{1.23456:.2f}") 
  # 소수점 3번째에서 반올림해서 2번째 자릿수까지만 출력하겠다.
  ```



- 이분탐색

  ```python
  def binary_search(array, target, start, end):
      while start <= end:
          mid = (start + end) // 2
          
          if mid == target:
              return mid
          elif array[mid] < target:
              start = mid + 1
          else:
              end = mid - 1
      return None
  
  ##################################################
  from bisect import bisect_right, bisect_left
  # 각각 원하는 값이 들어갈때 왼쪽 위치와 오른쪽 위치를 반환
  bisect_right(array, value) => 들어갈 위치의 오른쪽 index를 return
  bisect_left(array, value) => 들어갈 위치의 왼쪽 index를 return
  ```



- 다이나믹프로그래밍

  => 코테에서 과연 해당 문제가 DP문제인지 파악하는 방법

  => 그리디, 구현, 완전 탐색 등의 아이디어로 해결되지 않을 때 DP인지 의심하기

  => 해당 문제가 부분문제로 구성되어 있는지 확인

  => 부분문제? => 하나의 문제가 같은 과정의 똑같은 문제로 반복될 수 있는지

  => 해당 문제의 DP테이블 값을 구할 때 같은 과정을 계속 반복하는 경우 찾기

  => DP테이블에서 해당 값 == 해당 값까지 왔을 때의 경우(이전 값들도 동일한 과정임)

  => 이를 통해 DP테이블을 만들어 놓고 매번 갱신하면서 채워나감

  => DP에는 LIS, Knapsack, 플로이드-워샬 알고리즘이 있다.(기본적으로 암기해줘야함)



- 분할정복



- 다익스트라 알고리즘, 플로이드워샬



- 위상정렬



- 크루스칼 알고리즘



- 스택, 큐, 힙 구조(자료구조)를 활용할 수 있는지 파악하기

  => 스택은 push, pop

  => 큐는 popleft

  => 힙은 heappush, heappop, heapify(list) + 최대, 최소 값 구할 때 활용방안 생각하기
  
  ```python
  import heapq
  tmp = [1, 5, 7, 2, 4, 6]
  heapq.heapify(tmp) # => tmp리스트를 heap으로 만들어버림 + return 없음
  ```
  
  

- defaultdict

  => dict인데 기본 세팅을 설정할 수 있는 dict

  ```python
  from collections import defaultdict
  list_dict = defaultdict(list)
  
  for key, value in clothes:
  	list_dict[key].append(value)
  
  # list_dict = {'key' : [value1, value2, value3]}
  ```



- deque 회전시키기 => rotate()

  => deque.rotate(방향)

  ```python
  from collections import deque
  
  q = deque([1, 2, 3, 4, 5])
  
  q.rotate(방향과 칸)
  
  # 오른쪽으로 1칸 이동 
  q.rotate(1)
  # q = [5, 1, 2, 3, 4]
  
  # 왼쪽으로 1칸 이동 
  q.rotate(-1)
  # q = [2, 3, 4, 5, 1]
  
  # rotate()를 사용하지 않고 deque이기 때문에
  # tmp = q.popleft()		q.pop()
  # q.append(tmp)			q.appendleft(tmp)
  # 해도 같음
  # 하지만 rotate()의 장점은 => 방향 + 원하는 칸의 개수까지 한 번에 설정 가능하다는 점!
  ```



- sort() 함수 + lambda

  => python에서 대표적으로 정렬하는 함수

  ```python
  # 오름차순 정렬
  list.sort()
  
  # 내림차순 정렬
  list.sort(reverse=True)
  
  # lambda를 사용해서 다양한 조건 추가
  list.sort(key=lambda x:x[0])
  
  # 여러개 조건 추가
  list.sort(reverse=True, key=lambda x:(len(x), x[1]))
  
  
  # 딕셔너리 정렬 => money의 value를 기준으로 오름차순 정렬
  money = { "백원" : 100, "1$" : 1200, "10$" : 12000, "오천원" : 5000, "만원" : 10000, "100$" : 120000, "오만원" : 50000 } 
  
  # => money.items()를 추가해서 key와 value의 튜플로 x를 받아내는 것이 핵심
  money = sorted(money.items(), key = lambda x : x[1]) 
  
  # 출력 값 
  [('백원', 100), ('1$', 1200), ('오천원', 5000), ('만원', 10000), ('10$', 12000), ('오만원', 50000), ('100$', 120000)]
  ```



- 숫자를 문자열로 바꾸어서 비교

  ```python
  # [3, 30, 34, 5, 9] => [9, 5, 34, 3, 30]으로 만드는 방법
  # 해당 value가 최대 1000이라고 가정할 때 각각의 value에 *3을 해서 3자리로 맞춰준다. 
  numbers.sort(reverse=True, key=lambda x:x*3)
  ```



- 문자열 조건으로 찾기(startswith(), endswith(), find())

  ```python
  s = 'abcdefg'
  
  # s.find('value')
  # => 찾으면 해당 idx 없으면 -1
  s.find('a') => 0
  
  # s.startswith('value')
  # => 'value'로 시작하면 True / False
  s.startswith('a') => True
  
  # s.endswith('value')
  # => 'value'로 끝나면 True / False
  s.endswith('a') => False
  ```



- enumerate(list) 활용하기

  => enumerate(list)는 해당 리스트의 값과 인덱스 값을 동시에 보여준다.

  => for idx, value in enumerate(list):



- for ~ else ~ 구문

  => for문 안에서 break로 멈추지 않아야 else문이 작동함

  => 따라서, else문을 사용하기 위해서는 for문 안에 break가 있어야 함



- stack 자료구조

  => 생각보다 많이 등장함

  => stack.append()해서 새로운 값과 stack[-1]를 비교하고 stack.pop()하는 형태의 문제

  => 문자열이나 리스트의 값을 하나씩 돌면서 앞, 뒤 값과 비교해서 처리해야하는 문제 style



- heap 자료구조

  => 최대, 최소 값을 매번 구해야하는 경우 사용하면 시간을 줄일 수 있음

  => sort()나 min, max를 사용하는 것보다 heap자료에 리스트를 넣는다

  => heapq.heapify(list) => heap으로 바뀜

  => 해당 heap으로 바뀐 리스트 tmp는 매번 알아서 최소, 최대 힙으로 정렬된다.

  => 따라서 가장 작은 값은 min(tmp)가 아니라 그냥 => tmp[0]이 가장 작은 값이다(왜? 알아서 정렬됨)



- subset()

  => 부분집합 구하기

  => 더하거나 빼거나 / 추가하거나 추가하지 않거나 

  => 원하는 Level까지 내려가면서 선택해야하는 모든 경우

  ```python
  # subset
  arr = [1, 2, 3]
  def subset(L, ss):
      if L == len(arr):
          print(*ss)
          return
      else:
          subset(L+1, ss + [arr[L]])
          subset(L+1, ss)
  
  subset(0, [])
  ```



- 2차원 리스트를 1 ~ n 으로 초기화 하기

  ```python
  board = [[0] * columns for _ in range(rows)]
  value = 0
  
  for i in range(rows):
      for j in range(columns):    
          value += 1
          board[i][j] = value
  ```

   
  
- 거리를 기록할 경우는 (출발-도착) + (도착+출발) 두 방향 전부 기록해준다

  => 추가적으로 중복을 제거할 때는 set()을 활용한다.



- 딕셔너리에서 items() 사용하기

  => for key, value in dict.items():

  => 으로 각각의 key와 value 쌍으로 처리 가능



- 딕서너리에서 sort() 하는 법

  => tmp  = sorted(dict.items(), key=lambda x: x[1], reverse=True)



- 하나의 문자열을 여러개로 분류할 때

  => 2 덩어리

  => if else

  => 3 덩어리

  => if elif else

  ```python
  # 카카오 - 문자열 정렬
      for file in files:
          head = ''
          number = ''
          tail = ''
          check = False
          for i in range(len(file)):
              if file[i].isdigit():
                  number += file[i]
                  check = True
              elif not check:
                  head += file[i]
              else:
                  tail = file[i:]
                  break
                    
          sliced.append((head, number, tail))
  ```



- 여러 개의 조건으로 sort() 할때

  => list.sort(key=lambda x: (x[0], x[1]))

  => 이때 x[0]에서 같은 값이 나오는 경우만 x[1]조건이 적용된다.

  => 추가적으로 sort()안에서도 함수 적용가능

  => list.sort(key=lambda x:(x[0].upper(), int(x[1])))



- 문제가 단순해서 풀었는데 시간초과?

  => 해당 문제는 그냥 단순 구현이 아닌 규칙을 찾아야 하는 경우가 있음

  => 짝수, 홀수 경우로 나눠서 시도해 보기 - 2개 이하로 다른 비트 문제



- 직접 list를 전부 순회해서 탐색하는 방법이 시간초과가 날때

  => 효율성을 위해 딕셔너리와 이분탐색을 이용하는 것이 빠르다

  => 이때, 딕셔너리는 나올 수 있는 경우를 모두 기록한다.

  => 이때, 이분탐색은 정렬된 상태에서 빠르게 원하는 값을 찾을 수 있다

  => 결론 : 딕셔너리 + 이분탐색 조합 => 빠름



- 앞에서도 말했지만 생각보다 defaultdict 많이 사용함



- 이분탐색을 쉽게하기 위해

  => 정렬이 전제

  => 방법1 : 직접 코드를 짜는 방법

  => 방법2 : from bisect import bisect_left, bisect_right 



- set에서 사용하는 함수

  => add(값) - 집합에 새로운 값을 추가한다. (중복된 값은 무시)

  => remove(값) - 전달받은 값을 삭제 (없을 때 에러 메시지를 출력)

  => discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)

  => clear() - 집합에 있는 모든 값을 삭제

  => &, intersection -  교집합
  
  => set1.issubset(set2) - set1이 set2의 부분집합인지 True / False



- 중복조합

  => 지금까지 itertools를 사용하면서 permutations, combinations, product는 많이 사용했지만

  => 중복조합은 사용한 적이 없음

  => from itertools import combinations_with_replacement 로 사용

  => for comb in list(combinations_with_replacement(list, n))



- enumterate안에 zip넣기

  => 두 개의 list의 값들을 동시에 꺼낼때!!!(생각보다 많이 씀)

  => 이때 두 list는 서로 크기가 같아야 한다!!(enumterate의 idx 값 때문)

  => for i, (a, b) in enumerate(zip(listA, listB))



-  중복된 값을 지울때 set()을 활용한다(자주 사용)

  => 하지만 중복된 좌표를 지울 때는 이상하게 잘 안씀..!!!

  => 중복된 좌표를 지울 때도 set()활용하기 + len(set())는 중복이 없는 값의 크기



- 2차원 리스트를 당기는 문제 - 프렌즈 4블럭 or 테트리스 같은 문제

  => 2차원 리스트를 한 줄 씩 돌면서 필요없는 값을 지우고 마지막에 지운만큼 append()하거나

  => 그대로 좌표값을 이용해서 i => i + 1으로 내리고 기존의 i값은 새로운 값으로 갱신(대신 i는 해당 리스트의 맨 위부터 순회하면서 아래로 내려간다)



- 위의 2차원 리스트를 당길때(1번 방법)

  => 2차원 리스트 순회를 col 먼저 하면 어려움!!

  => 이때는 그냥 리스트 자체를 90도 회전하고 row로 바꾼뒤에 해결하는 방법이 편함

  => 문제를 보고 무작정 구현하려는 것보단 쉬운방법으로 바꿀 수 있는지 고민 후 접근하기!!!!!!



- 하나의 문자열 안에서 문자를 돌면서 원하는 조건을 찾아낼 때는 역시

  => stack 를 이용한다!



- 리스트에서 원하는 개수 만큼 뽑고 넣고 할때 - 괄호 변환

  => for i in range(len(list))로 하면 index out of range 에러가 쉽게 발생함

  => pop 하고 append하는 과정에서 리스트의 전체 크기가 복잡해짐

  => 따라서 이럴때는 while len(list) != 0 으로 한다

  => while문을 활용하면 리스트 전체의 크기가 변하더라도 크기를 직접 고려하지 않고 다 뺄 수 있음!! 



- 원하는 조건으로 주어진 문자열을 다시 조립할 때

  => 반드시 마지막 문자를 따로 추가해 준다 - 수식 최대화

  ```python
  # 카카오 수식 최대화
  
  expression = "100-200*300-500+20"
  for e in expression:
      if e.isdigit():
          tmp += e
      else:
          changed.append(tmp)
          tmp = ''
          changed.append(e)
          temp.add(e)
  # 이 부분! => 따로 추가하지 않으면 마지막 문자는 changed 리스트에 추가되지 않는다.
  changed.append(tmp)
  
  changed = ["100", "-", "200", "*", "300", "-", "500", "+", "20"]
  ```



- 최대한 기능들을 나눠서 함수단위로 작성하자

  => 그래야 보기도 구현하기도 편함 + 변수명작성도 편함



- 재귀 구조 잘 파악하기!

## 2. Level 2 에서 다시 풀어볼 만한 문제

- 땅따먹기 - DP... => 브루트 포스인줄 알았지만.. 아님
- 가장 큰 정사각형 찾기 - DP
- 모음사전 - 중복순열
- 전력망 둘로 나누기 - union-find로 풀 수 있을 것 같은데...
- 큰 수 만들기 - stack자료구조
- 조이스틱 - 문제는 탐욕법이라는데... 완탐...
- 가장 큰 수 - 특이한 문제
- 124 나라의 숫자 - 진법 변환과 비슷...
- 멀쩡한 사각형 - 그냥 수학문제
- 기능 개발 - 스택/큐 문제라고 하는데 글세... => 워하는 값이 나오면 모아놨다가 누적하는 문제
- 타겟 넘버 - 기본적인 subset문제
- 2개 이하로 다른 비트 - 규칙찾기



- 카카오
  - 문자열 정렬 - 여러개의 조건으로 sort()
  - 순위 검색 - 효율성 문제 때문에..!! 해싱 + 이분탐색
  - 후보키 - CS관련 : 유일성과 최소성에 대해!!
  - 양궁대회 - 완전탐색, 중복조합
  - 프렌즈 4블럭 - 다풀었는데 5번 테스트 케이스만 이상하게 실패...
  - 괄호 변환 - 구현문제 + 재귀
