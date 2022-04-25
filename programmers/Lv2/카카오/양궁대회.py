# 중복순열...!!! + enumerate안에 zip 넣기(이때 zip안에 들어가는 두 리스트는 크기가 같아야함)
# from itertools import combinations_with_replacement 

from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    gap = -2147000000
    win = False
    for comb in combinations_with_replacement(range(11), n):
        now = [0] * 11
        for co in comb:
            now[10-co] += 1
        
        lion = 0
        apeach = 0
        
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            elif p >= l:
                apeach += (10 - i)
            else:
                lion += (10 - i)
        
        if lion > apeach :
            win = True
            tmp = lion - apeach 
            if tmp > gap:
                gap = tmp
                answer = now
        if not win:
            answer = [-1]
    return answer