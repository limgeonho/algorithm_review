import pprint

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# q = []
#
# board = [[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0]]
#
# for i in range(4):
#     for j in range(4):
#         if board[i][j] == 1:
#             q.append((i, j))
#
# while q:
#     now_x, now_y = q.pop(0)
#     for k in range(4):
#         nx = now_x + dx[k]
#         ny = now_y + dy[k]
#         if 0<=nx<4 and 0<=ny<4 and board[nx][ny] == 0:
#             board[nx][ny] = board[now_x][now_y] + 1
#             q.append((nx, ny))
#
# print(board)

q = []
board = [[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
visited = [[-1] * len(board[0]) for _ in range(len(board))]

q.append((0, 0))
visited[0][0] = 0

while q:
    now_x, now_y = q.pop(0)
    for k in range(4):
        nx = now_x + dx[k]
        ny = now_y + dy[k]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and visited[nx][ny] == -1 and board[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = visited[now_x][now_y] + 1

pprint.pprint(visited)
