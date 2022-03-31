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

arr = list(range(1, n+1))
visited = [False] * len(arr)
res = [0] * m
cnt = 0

perm(0)
print(cnt)