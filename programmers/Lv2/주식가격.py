def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        tmp = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                tmp += 1
            else:
                break
        answer.append(tmp)
    return answer + [0]