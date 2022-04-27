def solution(n):
    answer = 0
    tmp = [0] * 2001
    tmp[1] = 1
    tmp[2] = 2
    for i in range(3, len(tmp)):
        tmp[i] = tmp[i-1] + tmp[i-2]
    print(tmp[4])
    answer = tmp[n] % 1234567
    return answer