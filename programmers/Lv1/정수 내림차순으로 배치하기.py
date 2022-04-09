def solution(n):
    print(type(n))
    answer = 0
    tmp = list(str(int(n)))
    tmp.sort(reverse=True)
    answer = int(''.join(tmp))
    return answer