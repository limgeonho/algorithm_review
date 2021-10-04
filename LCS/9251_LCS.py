# LCS

w_1 = input()
w_2 = input()

n = len(w_1)
m = len(w_2)

w_1 = ' ' + w_1
w_2 = ' ' + w_2

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if w_1[i] == w_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])