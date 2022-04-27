# 답은 나오는데 효율성에서 틀리는 문제 => 당연한 결과..
from itertools import permutations
def solution(n, k):
    answer = []
    tmp = 0
    for perm in permutations(range(1, n+1), n):
        tmp += 1
        if tmp == k:
            answer = list(perm)
            break
    return answer

####################################################################
# 수학적으로 분류해보고 풀어야하는 문제였음..!
from math import factorial

def solution(n, k):
    answer = []
    tmp = list(range(1, n+1))
    
    while n != 0:
        fact = factorial(n-1)
        answer.append(tmp.pop((k-1)//fact))
        n -= 1
        k %= fact
    
    return answer
