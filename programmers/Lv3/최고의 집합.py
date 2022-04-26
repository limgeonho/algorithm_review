def solution(n, s):
    answer = []
    temp = []
    if n > s:
        answer = [-1]
        return answer
    if s % n == 0:
        tmp = s // n
        for _ in range(n):
            answer.append(tmp)
    else:
        tmp = s // n
        for _ in range(n):
            temp.append(tmp)
        gap = s - sum(temp)
        for i in range(1, gap+1):
            temp[-i] += 1
        answer = temp
    return answer