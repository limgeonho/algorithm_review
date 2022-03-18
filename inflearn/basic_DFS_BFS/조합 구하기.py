def comb(L, start):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
        return
    for i in range(start, len(arr)):
        res[L] = arr[i]
        comb(L+1, i+1)


n, m = map(int, input().split())
arr = range(1, n+1)
res = [0] * m
cnt = 0

comb(0, 0)
print(cnt)