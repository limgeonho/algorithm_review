def solution(price, money, count):
    answer = 0
    tmp = 0
    for i in range(1, count+1):
        tmp += price * i
    
    if money > tmp:
        return 0
    answer = tmp - money
    return answer