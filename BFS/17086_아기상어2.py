# 아기 상어2
# 상어끼리 거리를 구하는게 아니라 각 칸에서 가장 가까운 상어까지의 거리 중에 가장 큰 값 찾기...
# 문제 잘 읽기...
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        for k in range(8):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[now_x][now_y] + 1
                if board[nx][ny] == 1:
                    return visited[now_x][now_y] + 1

    return 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 모든 칸에서 순회 시작
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            tmp = bfs(i, j)
            # 최대값 갱신
            if answer < tmp:
                answer = tmp

print(answer)



