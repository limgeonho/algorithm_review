from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m =  map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))

q = deque()

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
           q.append((i, j))

while q:
    now_x, now_y = q.popleft()
    for k in range(4):
        nx = now_x + dx[k]
        ny = now_y + dy[k]
        if 0<=nx<m and 0<=ny<n and board[nx][ny] == 0:
            board[nx][ny] = board[now_x][now_y] + 1
            q.append((nx, ny))

res = -2147000000
for i in range(m):
    for j in range(n):
        if board[i][j] > res:
            res = board[i][j]-1

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            res = -1

print(res)