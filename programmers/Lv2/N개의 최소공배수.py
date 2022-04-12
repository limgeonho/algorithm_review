from math import gcd

def solution(arr):
    answer = 0
    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp = (tmp * arr[i]) // gcd(tmp, arr[i])
    answer = tmp
    return answer