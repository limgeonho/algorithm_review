from math import gcd
def solution(n, m):
    answer = []
    tmp = gcd(n, m)
    answer.append(tmp)
    answer.append(n*m//tmp)
    
    return answer