# Charm Bracelet

n, m = map(int, input().split())
dp = [0] * (m+1)

for i in range(n):
    weight, desirability = map(int, input().split())
    for j in range(m, weight-1, -1):
        dp[j] = max(dp[j], dp[j - weight] + desirability)

print(max(dp))