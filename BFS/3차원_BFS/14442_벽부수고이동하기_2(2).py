# 벽 부수고 이동하기2(2)

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    visited[a][b][c] = 1

    while q:
        x, y, z = q.popleft()
        for v in visited:
            print(v)
        print()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if z+1 <= k and board[nx][ny] == 1 and visited[nx][ny][z+1] == 0:
                    q.append((nx, ny, z+1))
                    visited[nx][ny][z+1] = visited[x][y][z] + 1

n, m, k = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

bfs(0, 0, 0)

answer = []
if visited[-1][-1] == [0] * (k+1):
    print(-1)
else:
    for i in range(k+1):
        if visited[-1][-1][i] != 0:
            answer.append(visited[-1][-1][i])
    print(min(answer))