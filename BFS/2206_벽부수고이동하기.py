# 벽 부수고 이동하기
from collections import deque
import pprint
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
            if z == 0 and board[nx][ny] == 1 and visited[nx][ny][z+1] == 0:
                visited[nx][ny][z+1] = visited[x][y][z] + 1
                q.append((nx, ny, z+1))


if visited[-1][-1][0] != 0 and visited[-1][-1][1] != 0:
    print(min(visited[-1][-1]))
elif visited[-1][-1][0] != 0:
    print(visited[-1][-1][0])
elif visited[-1][-1][1] != 0:
    print(visited[-1][-1][1])
else:
    print(-1)