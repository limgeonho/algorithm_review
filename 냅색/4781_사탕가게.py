# 사탕 가게


while True:
    n, m = map(float, input().split())
    n = int(n)
    m = int(m*100+0.5)
    dp = [0] * (m+1)

    if n == 0 and m == 0:
        break

    for i in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p*100+0.5)
        for j in range(p, m+1):
            dp[j] = max(dp[j], dp[j - p] + c)

    print(dp[m])