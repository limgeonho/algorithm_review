def solution(lottos, win_nums):
    answer = []
    tmp = 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            tmp += 1
    answer.append(rank[tmp+zero])
    answer.append(rank[tmp])
    
    return answer