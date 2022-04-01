from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        if now_x == 6 and now_y == 6:
            break
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<=6 and 0<=ny<=6 and visited[nx][ny] == -1 and board[nx][ny] == 0:
                visited[nx][ny] = visited[now_x][now_y] + 1
                q.append((nx, ny))


board = [[] * 7 for _ in range(7)]
for i in range(7):
    board[i] = list(map(int, input().split()))
visited = [[-1] * 7 for _ in range(7)]
bfs(0, 0)
print(visited[-1][-1])
