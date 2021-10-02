# 수강 과목

limit, n = map(int, input().split())
dp = [0] * (limit+1)

for i in range(n):
    value, importance = map(int, input().split())
    for j in range(limit, importance-1, -1):
        dp[j] = max(dp[j], dp[j-importance] + value)


print(max(dp))