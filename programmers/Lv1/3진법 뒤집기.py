def change(n):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, 3)
        tmp += str(mod)
    return tmp

def solution(n):
    answer = 0
    tmp = change(n)
    answer = int(tmp, 3)
    return answer