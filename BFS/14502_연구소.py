# 연구소
# 2차원 리스트의 조합 구하기 => 브루트포스

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(board):
    n = len(board)
    m = len(board[0])
    tmp = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            tmp[i][j] = board[i][j]
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for x1 in range(n):
    for y1 in range(m):
        if board[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if board[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if board[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        board[x1][y1] = 1
                        board[x2][y2] = 1
                        board[x3][y3] = 1
                        cur = bfs(board)

                        if answer < cur:
                            answer = cur

                        board[x1][y1] = 0
                        board[x2][y2] = 0
                        board[x3][y3] = 0

print(answer)
