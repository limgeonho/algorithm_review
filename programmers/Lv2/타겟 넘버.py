def subset(L, ss, numbers, target):
    global answer
    if L == len(numbers):
        if ss == target:
            answer += 1
            return 
    else:
        subset(L+1, ss + numbers[L], numbers, target)
        subset(L+1, ss - numbers[L], numbers, target)

answer = 0
def solution(numbers, target):
    
    subset(0, 0, numbers, target)
    return answer