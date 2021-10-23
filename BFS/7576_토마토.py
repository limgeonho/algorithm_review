# 토마토
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(q):
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                board[nx][ny] = board[now_x][now_y] + 1
                q.append((nx, ny))


m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

q = deque()
answer = []

for i in range(n*m):
    x = i // m
    y = i % m
    if board[x][y] == 1:
        q.append((x, y))

bfs(q)

for i in range(n*m):
    x = i // m
    y = i % m
    if board[x][y] == 0:
        print(-1)
        break
    else:
        answer.append(board[x][y])
else:
    print(max(answer)-1)
