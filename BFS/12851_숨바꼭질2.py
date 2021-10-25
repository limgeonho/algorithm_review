# 숨바꼭질2

from collections import deque

n, k = map(int, input().split())
board = [[-1, 0] for _ in range(100001)]

q = deque()
q.append(n)
board[n][0] = 0
board[n][1] = 1

while q:
    now = q.popleft()
    if now == k:
        break
    for nxt in (now+1, now-1, now*2):
        if 0<=nxt<=100000:
            if board[nxt][0] == -1:
                board[nxt][0] = board[now][0] + 1
                board[nxt][1] += 1
                q.append(nxt)
            elif board[nxt][0] == board[now][0] + 1:
                board[nxt][1] += 1
                q.append(nxt)

print(board[k][0])
print(board[k][1])