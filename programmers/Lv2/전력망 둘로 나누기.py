from itertools import combinations

def solution(n, wires):
    answer = -1
    
    for comb in combinations(wires, n-2):
        print(comb)
    
    return answer