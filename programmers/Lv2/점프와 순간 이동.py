# def solution(n):
#     ans = 0
#     tmp = bin(n).count('1')
#     ans = tmp

#     return ans

def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans