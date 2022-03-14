# 4578	[1, 4, 99, 35, 50, 1000]	2308
# 1999	[2, 11, 20, 100, 200, 600]	2798

money = 4578
costs = [1, 4, 99, 35, 50, 1000]

def solution(money, costs):
    answer = 0
    tmp1 = []
    tmp2 = 0

    for i in range(len(costs)):
        tmp3 = money // costs[i]
        for j in range(tmp3, -1, -1):
            money = money - (costs[i] * j)
            tmp1.insert(i, j)
        if money == 0:
            tmp1 = []
            print(tmp1)
    return answer