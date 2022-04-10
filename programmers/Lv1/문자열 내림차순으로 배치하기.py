def solution(s):
    answer = ''
    tmp = list(s)
    tmp.sort(reverse=True)
    answer = ''.join(tmp)
    return answer