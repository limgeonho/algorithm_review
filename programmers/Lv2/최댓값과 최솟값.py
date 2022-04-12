def solution(s):
    answer = ''
    s = list(map(int, s.split()))
    maxN = max(s)
    minN = min(s)
    answer = str(minN) + ' ' + str(maxN)
    return answer