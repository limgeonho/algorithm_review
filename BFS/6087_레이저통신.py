# 레이저 통신

# from collections import deque

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = 0
#     while q:
#         now_x, now_y = q.popleft()
#         for k in range(4):
#             nx = now_x + dx[k]
#             ny = now_y + dy[k]
#             # 벽이나 지도의 끝부분까지 계속 전진
#             while 0<=nx<h and 0<=ny<w:
#                 if board[nx][ny] == '*':
#                     break
#                 if visited[nx][ny] == -1:
#                     visited[nx][ny] = visited[now_x][now_y] + 1
#                     q.append((nx, ny))
#                 nx += dx[k]
#                 ny += dy[k]
#
#
#
# w, h = map(int, input().split())
# board = [list(map(str, input())) for _ in range(h)]
# visited = [[-1] * w for _ in range(h)]
# start = []
#
# for i in range(h):
#     for j in range(w):
#         if board[i][j] == 'C':
#             start.append((i, j))
#
# destination = start[1]
#
# bfs(start[0][0], start[0][1])
#
# print(visited[destination[0]][destination[1]]-1)
# for v in visited:
#     print(v)
# print()

############################################################################
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            while 0<=nx<h and 0<=ny<w:
                if board[nx][ny] == '*':
                    break
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx, ny))
                nx += dx[k]
                ny += dy[k]


w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]
visited = [[-1]*w for _ in range(h)]

spot = []

for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            spot.append((i, j))

sx, sy = spot[0][0], spot[0][1]
ex, ey = spot[1][0], spot[1][1]

bfs(sx, sy)
print(visited[ex][ey] - 1)
