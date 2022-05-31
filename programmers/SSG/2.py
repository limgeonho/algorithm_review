import heapq
def solution(v, a, b):
  answer = 0
  cnt = 0
  truck = v[:]
  heapq.heapify(v)
  while True:
    maxV = heapq.nlargest(n = 1, iterable=truck)  
    minV = heapq.nsmallest(n = 1, iterable=truck)
    if int(*maxV) < a or int(*minV) < b:
      break
    truck.remove(int(*maxV))
    truck.append(int(*maxV) - a)
    truck.remove(int(*minV))
    truck.append(int(*minV) - b)
    cnt += 1
  answer = cnt - 1 
  return answer 

v2 = [4,4,3]
v = [4, 5, 5]
a = 2
b = 1
print(solution(v, a, b))