# 벽 부수고 이동하기4
#
# from collections import deque
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs(x, y):
#     global cnt
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#
#     while q:
#         now_x, now_y = q.popleft()
#         cnt += 1
#         for k in range(4):
#             nx = now_x + dx[k]
#             ny = now_y + dy[k]
#             if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and not visited[nx][ny]:
#                 q.append((nx, ny))
#                 visited[nx][ny] = True
#
#
# n, m = map(int, input().split())
# board = [list(map(int, input())) for _ in range(n)]
# answer = [[0] * m for _ in range(n)]
#
# for i in range(n*m):
#     x = i // m
#     y = i % m
#     if board[x][y] == 0:
#         continue
#     else:
#         visited = [[False] * m for _ in range(n)]
#         cnt = 0
#         board[x][y] = 0
#         bfs(x, y)
#         answer[x][y] = cnt % 10
#         board[x][y] = 1
#
# for ans in answer:
####################################################################
# 시간 초과... => 플러드 필 만들기
# 중복되는 것들을 여러번 조사해야한다? => 한 번만 연산하고 연산 값을 저장해 두었다가 나중에 활용!
# 단지 번호 붙이기 처럼 numbering과 해당 numbering의 cnt를 기록해준다
# => 1이 인접한 numbering의 cnt들을 누적해준다!

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    g = len(group_size)
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    group[x][y] = g
    cnt = 1

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                group[nx][ny] = g
                cnt += 1
    group_size.append(cnt)


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
group = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
group_size = []


for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

# print(group_size)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans % 10, end='')
    print()