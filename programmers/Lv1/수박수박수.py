def solution(n):
    answer = ''
    tmp = n//2
    if n % 2 == 0:
        answer = "수박" * tmp
    else:
        answer = ("수박" * tmp) + "수"
    return answer