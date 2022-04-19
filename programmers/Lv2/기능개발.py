from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 1
    cnt = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while True:
        if not progresses:
            break
        if progresses[0] + (speeds[0] * day) >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                day += 1
                
    answer.append(cnt)
    
    return answer