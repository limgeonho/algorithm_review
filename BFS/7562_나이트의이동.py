# 나이트의 이동
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    cnt = 0
    while q:
        now_x, now_y = q.popleft()
        if now_x == ex and now_y == ey:
            return
        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[now_x][now_y] + 1
                q.append((nx, ny))

T = int(input())

for _ in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * n for _ in range(n)]

    bfs(sx, sy)

    print(visited[ex][ey])