from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, limit):
    q = deque()
    q.append((x, y))

    while q:
        now_x, now_y = q.popleft()
        for l in range(4):
            nx = now_x + dx[l]
            ny = now_y + dy[l]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] > limit:
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

res = -2147000000

for k in range(1, 101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > k:
                visited[i][j] = True
                bfs(i, j, k)
                cnt += 1
    if cnt > res:
        res = cnt

print(res)