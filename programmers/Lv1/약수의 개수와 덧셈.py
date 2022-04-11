def check(n):
    if (n**0.5) % 1 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if check(num):
            answer -= num
        else:
            answer += num
    return answer