def perm_with(L):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
        return
    for i in range(len(arr)):
        res[L] = arr[i]
        perm_with(L+1)

n, m = map(int, input().split())
arr = list(range(1, n+1))
res = [0] * m
cnt = 0

perm_with(0)
print(cnt)