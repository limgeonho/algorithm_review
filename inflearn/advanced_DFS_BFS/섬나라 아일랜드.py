from collections import deque

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(8):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))

n = int(input())
board = []
cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)