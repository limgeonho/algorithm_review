# 미로 찾기
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny] == '1':
                q.append((nx,ny))
                visited[nx][ny] = visited[now_x][now_y] + 1


n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

bfs(0, 0)

print(visited[-1][-1])