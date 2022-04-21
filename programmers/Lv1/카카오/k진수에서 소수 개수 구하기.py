def change(x, k):
    tmp = ''
    while x > 0:
        x, mod = divmod(x, k)
        tmp += str(mod)
    return tmp[::-1]

def isPrime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        else:
            return True
        
def solution(n, k):
    answer = 0
    tmp = change(n, k)
    check = list(map(str, tmp.split('0')))
    for ch in check:
        if ch:
            if isPrime(int(ch)):
                answer += 1
        else:
            continue
    return answer