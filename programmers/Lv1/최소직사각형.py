def solution(sizes):
    answer = 0
    tmp1 = []
    tmp2 = []
    for size in sizes:
        tmp1.append(max(size))
        tmp2.append(min(size))
        
    answer = max(tmp1) * max(tmp2)
    return answer