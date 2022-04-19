# 최대 최소값을 찾을 때 heap자료구조를 이용

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        mix = tmp1 + (tmp2 * 2)
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer