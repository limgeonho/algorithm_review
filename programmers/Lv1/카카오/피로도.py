from itertools import permutations

def solution(k, dungeons):
    answer = -2147000000
    for dg in permutations(dungeons, len(dungeons)):
        check = k
        cnt = 0
        for d in dg:
            if check >= d[0]:
                cnt += 1
                check -= d[1]
            else:
                break
        if answer < cnt:
            answer = cnt
    return answer