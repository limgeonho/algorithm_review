# 안녕

n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

limit = 99
dp = [0] * (limit+1)

for i in range(n):
    for j in range(limit, L[i]-1, -1):
        dp[j] = max(dp[j], dp[j-L[i]] + J[i])

print(max(dp))