# 해당 문제는 문제 풀이 접근을 잘못함...! 
# 나는 => reverse sort를 하고 하나씩 뺌
# 하지만 문제는 리스트의 가장 큰 수를 하나씩 빼는 거로 해결가능
# => 매번 max()를 해서 value를 뽑아내면 시간초과!
# => 당연히 매순간 정렬되는 heap 자료구조를 이용! 
# => 해당 문제에서는 max heap 구현

import heapq

def solution(n, works):
    if sum(works) < n:
        return 0
    
    answer = 0
    q = []
    
    for work in works:
        heapq.heappush(q, -work)
    
    while n != 0:
        tmp = -heapq.heappop(q)
        tmp -= 1
        heapq.heappush(q, -tmp)
        n -= 1
    
    while q:
        tmp = -heapq.heappop(q)
        if tmp <= 0:
            continue
        else:
            answer += tmp ** 2
    
    return answer