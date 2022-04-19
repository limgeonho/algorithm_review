
from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, value in enumerate(priorities):
        q.append((value, idx))
    tmp = 0
    while q:
        if len(q) == 1:
            q.popleft()
            tmp += 1
            break
        for i in range(1, len(q)):
            if q[0][0] < q[i][0]:
                t = q.popleft()
                q.append(t)
                break
        else:
            temp = q.popleft()
            tmp += 1
            if temp[1] == location:
                break
    answer = tmp
        
        
    return answer