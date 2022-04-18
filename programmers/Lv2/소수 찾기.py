from itertools import permutations

def check(x):
    if x == 1 or x == 0:
        return False
    
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    tmp = []
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            temp = int(''.join(list(perm)))
            if temp not in tmp:
                tmp.append(temp)
                if check(temp):
                    answer += 1
                
    return answer