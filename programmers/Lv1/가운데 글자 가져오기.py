def solution(s):
    answer = ''
    tmp = len(s)
    if tmp % 2 == 0:
        answer += s[tmp//2-1] + s[tmp//2]
    else:
        answer = s[tmp//2]
    return answer