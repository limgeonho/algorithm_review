from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    board[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt



n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

apart = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 1
            tmp = bfs(i, j)
            apart.append(tmp)

print(len(apart))
apart.sort()
for a in apart:
    print(a)