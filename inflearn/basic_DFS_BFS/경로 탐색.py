def dfs(x):
    global cnt
    check[x] = True
    if x == n:
        cnt += 1

    for i in graph[x]:
        if not check[i]:

            dfs(i)
            check[i] = False



n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
check = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dfs(1)
print(cnt)