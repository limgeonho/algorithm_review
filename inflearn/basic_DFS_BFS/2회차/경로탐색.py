def dfs(start):
    global cnt
    if start == n:
        cnt += 1
    visited[start] = True
    for i in board[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = False

n, m = map(int, input().split())

board = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)

cnt = 0
dfs(1)

print(cnt)