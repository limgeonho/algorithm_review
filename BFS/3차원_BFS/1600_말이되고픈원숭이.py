# 말이 되고픈 원숭이
import pprint
from collections import deque

dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 0

while q:
    x, y, c = q.popleft()
    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]
        nc = c + cost[i]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0:
            if nc <= k and visited[nx][ny][nc] == -1:
                visited[nx][ny][nc] = visited[x][y][c] + 1
                q.append((nx, ny, nc))

# pprint.pprint(visited)

answer = -1
for i in range(k+1):
    if visited[h-1][w-1][i] == -1:
        continue
    if answer == -1 or answer > visited[h-1][w-1][i]:
        answer = visited[h-1][w-1][i]

print(answer)