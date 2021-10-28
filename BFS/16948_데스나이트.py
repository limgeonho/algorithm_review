# 데스 나이트
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        if now_x == ex and now_y == ey:
            return
        for k in range(6):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[now_x][now_y] + 1

n = int(input())
visited = [[-1] * n for _ in range(n)]
sx, sy, ex, ey = map(int, input().split())

bfs(sx, sy)

print(visited[ex][ey])