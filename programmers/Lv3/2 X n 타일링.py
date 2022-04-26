def solution(n):
    answer = 0
    tmp = [0] * 60001
    tmp[0] = 1
    tmp[1] = 2
    for i in range(2, n):
        tmp[i] = (tmp[i-1] + tmp[i-2])%1000000007
    answer = tmp[n-1]
    
    return answer