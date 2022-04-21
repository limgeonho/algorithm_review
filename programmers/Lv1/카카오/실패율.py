def solution(N, stages):
    answer = []
    maxV = max(stages)
    total = len(stages)
    stage = {}
    
    for i in range(1, N+1):
        if total != 0:
            temp = stages.count(i)
            stage[i] = temp / total
            total -= temp
        else:
            stage[i] = 0

    print(stage)
    return sorted(stage, key=lambda x: stage[x], reverse=True)