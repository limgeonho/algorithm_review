def comb(answer, numbers, L, start, res):
    if L == 2:
        answer.append(sum(res))
        return
    for i in range(start, len(numbers)):
        res[L] = numbers[i]
        comb(answer, numbers, L+1, i+1, res)

def solution(numbers):
    answer = []
    numbers.sort()
    res = [0] * 2
    
    comb(answer, numbers, 0, 0, res)
    tmp = set(answer)
    answer = list(tmp)
    answer.sort()
    return answer