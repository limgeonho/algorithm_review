def solution(n):
    answer = 0
    check = [False] * (n+1)

    for i in range(2, int(n**0.5)+1):
        if not check[i]:
            j = 2
            while i * j <= n:
                check[i*j] = True
                j += 1
    for i in range(2, n+1):
        if not check[i]:
            answer += 1
    
    return answer