dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[x][y] < board[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False

n = int(input())
cnt = 0
board = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

s = 2147000000
e = -2147000000

for i in range(n):
    for j in range(n):
        s = min(board[i][j], s)
        e = max(board[i][j], e)

sx, sy = 0, 0
ex, ey = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == s:
            sx, sy = i, j
        if board[i][j] == e:
            ex, ey = i, j

visited[sx][sy] = True
dfs(sx, sy)

print(cnt)
