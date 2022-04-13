def count(x):
    tmp = bin(x)
    return tmp.count('1')

def solution(n):
    answer = 0
    tmp = count(n)
    while True:
        n += 1
        changed = count(n) 
        if tmp == changed:
            answer = n
            break
    return answer