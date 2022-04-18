def solution(clothes):
    answer = 0
    tmp = {}
    for cloth in clothes:
        tmp[cloth[1]] = tmp.get(cloth[1], 0) + 1

    temp = 1
    for a in tmp.values():
        temp *= (a+1)
    answer += (temp-1)
    
    return answer