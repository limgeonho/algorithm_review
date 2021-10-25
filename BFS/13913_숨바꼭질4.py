# 숨바꼭질4

from collections import deque

n, k = map(int, input().split())

board = [-1] * 100001
path = [-1] * 100001

q = deque()
q.append(n)
board[n] = 0
path[n] = n

while q:
    now = q.popleft()
    if now == k:
        break
    for nxt in (now+1, now-1, now*2):
        if 0<=nxt<=100000 and board[nxt] == -1:
            q.append(nxt)
            board[nxt] = board[now] + 1
            path[nxt] = now


print(board[k])
answer = [k]
tmp = path[k]
for _ in range(board[k]):
    answer.append(tmp)
    tmp = path[tmp]

print(*answer[::-1])