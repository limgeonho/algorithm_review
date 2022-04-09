def solution(n):
    answer = 0
    tmp = str(n)
    for t in tmp:
        answer += int(t)
    return answer