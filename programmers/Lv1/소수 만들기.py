from itertools import combinations

def check(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True
    
def solution(nums):
    answer = 0
    for comb in list(combinations(nums, 3)):
        if check(sum(comb)):
            answer += 1

    return answer