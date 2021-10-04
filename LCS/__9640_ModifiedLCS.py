# Modified LCS

t = int(input())

def make_arr(start, size, length):
    tmp = [start]
    for _ in range(length-1):
        tmp.append(tmp[-1] + size)
    return tmp

for _ in range(t):
    array = list(map(int, input().split()))
    n = array[0]
    m = array[3]

    arr_1 = make_arr(array[1], array[2], n)
    arr_2 = make_arr(array[4], array[5], m)

    arr_1 = [' '] + arr_1
    arr_2 = [' '] + arr_2

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr_1[i] == arr_2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n][m])