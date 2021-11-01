# 아기 상어
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(board, x, y, size):
    n = len(board)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and d[nx][ny] == -1:
                ok = False
                eat = False

                if board[nx][ny] == 0:
                    ok = True
                elif board[nx][ny] < size:
                    ok = True
                    eat = True
                elif board[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]


n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0

answer = 0
size = 2
exp = 0

while True:
    p = bfs(board, x, y, size)
    if p is None:
        break

    dist, nx, ny = p
    board[nx][ny] = 0
    answer += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0

    x, y = nx, ny

print(answer)