# 탈옥
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(board, x, y):
    visited = [[-1]*w for _ in range(h)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny] == -1 and board[nx][ny] != '*':
                if board[nx][ny] == '#':
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx, ny))
                else:
                    visited[nx][ny] = visited[now_x][now_y]
                    q.appendleft((nx, ny))
    return visited


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    board = ['.' + input() + '.' for _ in range(h)]
    # board를 임의로 늘렸으니 w, h도 크기를 늘려준다.
    h += 2
    w += 2
    board = ['.' * w] + board + ['.' * w]

    d0 = bfs(board, 0, 0)

    prisoner = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '$':
                prisoner.append((i, j))

    d1 = bfs(board, prisoner[0][0], prisoner[0][1])
    d2 = bfs(board, prisoner[1][0], prisoner[1][1])
    answer = 987654321

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if board[i][j] == '#':
                cur -= 2
            answer = min(answer, cur)

    print(answer)