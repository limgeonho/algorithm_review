# def fibo(x):
#     if x <= 1:
#         return x
#     return fibo(x-1) + fibo(x-2)
# def solution(n):
#     answer = 0
#     n = n % 1234567
#     answer = fibo(n)
    
#     return answer
def solution(n):
    answer = 0
    arr = [0] * 100001
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    answer = arr[n] % 1234567
    return answer