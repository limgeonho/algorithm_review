def perm(L):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
        return
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = arr[i]
        perm(L+1)
        visited[i] = False


n, m = map(int, input().split())
arr = range(1, n+1)
res = [0] * m
visited = [False] * len(arr)
cnt = 0
perm(0)
print(cnt)