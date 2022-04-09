def solution(x):
    answer = True
    tmp = list(map(int, str(x)))
    if x % sum(tmp) == 0:
        pass
    else:
        answer = False
    return answer