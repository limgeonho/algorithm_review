# 벽 부수고 이동하기 3...끝판왕...!
# 기존의 벽을 부수는 회수에 제한 + 낮/밤으로 인한 추가 옵션

# from collections import deque
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs(a, b, c):
#     q = deque()
#     q.append((a, b, c, 1))
#     visited[a][b][c] = True
#     day = True
#     while q:
#         p = len(q)
#         for _ in range(p):
#             x, y, z, d = q.popleft()
#             # for v in visited:
#             #     print(v)
#             # print()
#             if x == n-1 and y == m-1:
#                 return d
#             for l in range(4):
#                 nx = x + dx[l]
#                 ny = y + dy[l]
#                 if 0<=nx<n and 0<=ny<m:
#                     if board[nx][ny] == 0 and not visited[nx][ny][z]:
#                         visited[nx][ny][z] = True
#                         q.append((nx, ny, z, d+1))
#                     if z+1<=k and board[nx][ny] == 1 and not visited[nx][ny][z+1]:
#                         if day:
#                             visited[nx][ny][z+1] = True
#                             q.append((nx, ny, z+1, d+1))
#                         else:
#                             q.append((x, y, z, d+1))
#         day = not day
#     return -1
#
# n, m, k = map(int, input().split())
# board = [list(map(int, input())) for _ in range(n)]
# visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]
# print(bfs(0, 0, 0))

# 벽 부수고 이동하기 3...끝판왕...!
# 기존의 벽을 부수는 회수에 제한 + 낮/밤으로 인한 추가 옵션

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    visited[a][b][c] = 1
    day = True
    while q:
        p = len(q)
        for _ in range(p):
            x, y, z = q.popleft()
            # for v in visited:
            #     print(v)
            # print()

            for l in range(4):
                nx = x + dx[l]
                ny = y + dy[l]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                        visited[nx][ny][z] = visited[x][y][z] + 1
                        q.append((nx, ny, z))
                    if z+1<=k and board[nx][ny] == 1 and visited[nx][ny][z+1] == 0:
                        if day:
                            visited[nx][ny][z+1] = visited[x][y][z] + 1
                            q.append((nx, ny, z+1))
                        # else:
                        #     visited[x][y][z] = visited[x][y][z] + 1
                        #     q.append((x, y, z))

                    if not day and board[nx][ny] == 1:
                        visited[x][y][z] = visited[x][y][z] + 1
                        q.append((x, y, z))
        day = not day
    return -1


n, m, k = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
tmp = []

bfs(0, 0, 0)
print(visited[-1][-1])