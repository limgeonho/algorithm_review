from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c, 1))
    visited[a][b][c] = True
    day = True
    while q:
        p = len(q)
        for _ in range(p):
            x, y, z, d = q.popleft()

            if x == n-1 and y == m-1:
                return d
            for l in range(4):
                nx = x + dx[l]
                ny = y + dy[l]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny] == 0 and not visited[nx][ny][z]:
                        visited[nx][ny][z] = True
                        q.append((nx, ny, z, d+1))
                    if z+1<=k and board[nx][ny] == 1 and not visited[nx][ny][z+1]:
                        if day:
                            visited[nx][ny][z+1] = True
                            q.append((nx, ny, z+1, d+1))
                        else:
                            q.append((x, y, z, d+1))
        day = not day
    return -1

n, m, k = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, 0))