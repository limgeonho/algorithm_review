# 뱀과 사다리 게임

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    board[start] = 0
    while q:
        now = q.popleft()
        for i in range(1, 7):
            nx = now + i
            if nx > 100:
                continue
            nx = nxt[nx]
            if 1<=nx<=100 and board[nx] == -1:
                board[nx] = board[now] + 1
                q.append(nx)


n, m = map(int, input().split())
board = [-1] * 101
nxt = list(range(101))

for _ in range(n+m):
    a, b = map(int, input().split())
    nxt[a] = b

bfs(1)

print(board[100])