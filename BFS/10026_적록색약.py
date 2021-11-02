# 적록색약
# 기본적인 같은 구역 개수를 찾는 bfs(섬 개수 문제와 비슷) + 특정 조건 추가
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True


n = int(input())
board = [list(input()) for _ in range(n)]

ans_1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            ans_1 += 1


# G과 R중 하나로 맞춰준다.
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'


# 지도가 달라졌기 때문에 visited를 다시 하나 만들어 준다.
visited = [[False] * n for _ in range(n)]
ans_2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            ans_2 += 1

print(ans_1, end=' ')
print(ans_2)

