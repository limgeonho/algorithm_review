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


####################################################################################################
'''
최단 경로 = bfs 내지 backtrack dfs(거리 갱신 귀찮음)
수정 >> 최단 경로 수 인줄 알았는데 경로 길이면 그냥 bfs
추가로 보낼 인자(벽 부수기 찬스 횟수, 낮/밤 상태) 
'''
import sys
input = sys.stdin.readline
from collections import deque

# 상수
MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    # 초기화 (x좌표, y좌표, 찬스 횟수, 낮(1)/밤(0)), 거리
    q = deque()
    q.append((0, 0, K, 1, 0))
    # 방문
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1

    while q:
        x, y, chance, breakable, dist = q.popleft()
        if x == M-1 and y == N-1:
            return dist + 1
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N:
                # 벽 아님(그냥 이동)
                if maps[ny][nx] == '0':
                    if not visited[ny][nx][chance]:
                        visited[ny][nx][chance] = 1
                        q.append((nx, ny, chance, (breakable + 1) % 2, dist+1))
                # 벽 이지만 찬스 남음
                elif chance:
                    if not visited[ny][nx][chance-1]:
                        # 낮이냐
                        if breakable:
                            visited[ny][nx][chance-1] = 1
                            q.append((nx, ny, chance-1, (breakable + 1) % 2, dist+1))
                        # 밤이면 대ㅡ기 하고 시간만 경과
                        else:
                            q.append((x, y, chance, (breakable + 1) % 2, dist+1))

    return -1

# 세로, 가로, 벽 부수기 찬스(낮)
N, M, K = map(int, input().split())
maps = [input().rstrip() for _ in range(N)]

print(bfs())