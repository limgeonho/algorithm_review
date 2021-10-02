# 벼락치기

n, limit = map(int, input().split())
dp = [0] * (limit+1)

for i in range(n):
    k, s = map(int, input().split())
    for j in range(limit, k-1, -1):
        dp[j] = max(dp[j], dp[j-k] + s)

print(max(dp))