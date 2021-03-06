## 프로그래머스 부수기[Lv 1]



## 1. Level 1

- .split() vs .split(' ')의 차이점

  => .split()는 /t까지 전부 공백의 개수와 상관없이 하나의 공백으로 처리함

  => .split(' ')는 딱 ' '사이의 1개의 공백만을 공백으로 처리함



- map함수

  => .map(function, iterable)

  => iterable는 list, tuple, str

  => 반환형은 map객체로 나오기 때문에 list나 tuple로 반환받는다

  => list(map(function, iterable)) or tuple(map(function, iterable))

  

- .join함수

  => '구분자'.join(list)

  => 반환형은 str임

  

- .remove함수

  => 리스트에서 원하는 인자를 제거 할때

  => list.remove('원하는 인자')

  

- 최대공약수

  => 유클리드 호제법 이용

  ```python
  # 유클리드 호제법
  # a, b의 최대공약수 == a, a를 b로 나눈 나머지의 최대 공약수
  def gcd(a, b):
  	while b > 0:
  		a, b = b, a % b
  	return a
  ```

  

- list, str의 slice

  => arr[-4:]

  => arr리스트의 끝에서 4번째부터 마지막까지를 의미

  => 슬라이싱의 기준을 음수(-)인 경우 고려

  

- list 복사하기

  => 단순하게 = 으로 복사하면 주소 값을 복사한다.

  ```python
  list1 = [1, 2, 3, 4]
  list2 = list1[:]
  # list2에 list1의 내용만 복사 완료
  ```



- 파이썬에서는 리스트나 문자열의 덧셈과 곱셈이 쉽다. => 아는 건데 왜 활용을 잘 안할까??

  => 'abc' * 2 = 'abcabc'

  => [a, b, c] + [d, e] = [a, b, c, d, e]



- 최대값, 최소값을 찾을 때 max, min말고 다른 방법 => heapq이용

  ```python
  import heapq
  
  # default 최소 힙
  q = []
  heapq.heappush(q, value)
  heapq.heappop(q) # 최소 값이 차례대로 나옴
  
  # 최대 힙
  heapq.heappush(q, -value)
  -heapq.heappop(q) # 최대 값이 차례대로 나옴
  
  ```

  

- 스택(stack)

  => stack = [1, 2, 3, 4]

  => stack[-1] = 4



- sort()에서 lambda함수

  => list.sort(key=lambda x : x[1])

  ```python
  # sort()함수는 default가 오름차순임
  
  a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
  
  # 두 번째 인자를 기준으로 오름차순
  b = sorted(a, key=lambda x : x[1])
  => b = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]
  
  # 첯 번째 인자를 기준으로 오름차순 + 두 번째 인자를 기준으로 내림차순(동시에 2가지 조건 적용)
  c = sorted(a, key=lambda x : (x[0], -x[1]))
  ```



- str의 lower(), upper() 함수

  => 'abcDE'.lower() 

  => 전체 소문자 변경

  => 원래 문자열에는 변화가 없기 때문에 새로운 변수에 할당 해야함

  => changed = 'abcDE'.lower()



- isdigit(), isalnum(), isalpha()



- list에서 원하는 인자의 idx 찾기

  => list.index('value')
  
  => 인덱스 값이 나옴
  
  => 없으면 에러
  
  => 여러 개면 가장 앞 인덱스



- 소수 구하기(에라토스테네스의 체)

  ```python
  check = [False] * (n+1)
  
  for i in range(2, int(n**0.5)+1):
  	if not check[i]:
  		j = 2
  		while i * j <= n:
  			check[i*j] = True
  			j += 1
  ```

  

- ord(), chr()함수

  => ord('a') == 97

  => chr(97) == 'a'



- set 자료구조

  => 집합 + 중복이 제거된다

  ```python
  # 선언하기
  tmp = set()
  
  # 추가하기
  tmp.add(value)
  
  # 제거하기
  tmp.remove(value)
  
  # 여러개의 값 추가하기
  tmp.update(values)
  
  # 교집합 구하기
  tmp1 = set()
  tmp2 = set()
  tmp1.intersection(tmp2)
  ```



- itertools 관련 함수

  => zip(), all(), any(), chain()

  ```python
  # 1. zip()
  # 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환
      z = zip([1, 2, 3], ('A', 'B', 'C'))
      print(next(z)) # (1, 'A')
      print(next(z)) # (2, 'B')
      print(next(z)) # (3, 'C')
  
  # 2. all()
  # iterable한 객체를 인수로 받아서 원소가 모두 참이면 True, 아니면 False를 반환
      a = all([1, 2, 3]) # True
      a = all([0, 1, 2]) # False
  
  # 3. any()
  # iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False를 반환
      a = any([0, 1, 2]) # True
      a = any([0, False, []] # False
  
  # 4. chain()
  #iterable한 객체들을 인수로 받아 하나의 iterator로 반환
      c1 = [1, 2]
      ca = ['A', 'B']
      c = itertools.chain(c1, ca)
      print(next(c)) # 1
      print(next(c)) # 2
      print(next(c)) # A
      print(next(c)) # B
  ```



- 루트안에 넣은 값이 자연수 인지 확인하는 방법
  1. int(num ** 0.5) == num ** 0.5
  2. (num ** 0.5) % 1 == 0



- 10진법으로 바꾸기

  => int('str', 현재의 진법)

  => int('22111', 3) => 10진법 229



- collections.Counter

  => 문자열이나 리스트의 요소를 카운팅해줌

  ```python
  from collections import Counter
  
  Counter('hello world') 
  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
  
  # 개수가 많은 요소부터 정렬
  Counter('hello world').most_common()
  
  # 개수가 가장 많은 요소 1개를 반환
  Counter('hello world').most_common(1)
  ```



- sort() vs sorted()

  => list.sort()는 return 값이 없고 해당 리스트를 정렬만함

  => sorted(list)는 정렬된 리스트를 return 함



- zip()

  => zip(listA, listB)

  => listA, listB에 들어가는 원소들을 차례대로 동시에 하나씩 뺄 수 있음



## 2. Level 1 에서 다시 풀어볼 만한 문제

- 체육복

  => 제한사항을 끝까지 잘 읽어야함...

  => 제한사항의 조건에 따라 기존에 문제에서 주어진 조건을 변경해야함

