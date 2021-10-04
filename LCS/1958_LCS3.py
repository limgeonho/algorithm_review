# LCS 3

def check(x, y, z):
    n = len(x)
    m = len(y)
    l = len(z)

    x = ' ' + x
    y = ' ' + y
    z = ' ' + z

    dp = [[[0] * (l+1) for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if x[i] == y[j] == z[k]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[n][m][l]


w_1 = input()
w_2 = input()
w_3 = input()

print(check(w_1, w_2, w_3))


