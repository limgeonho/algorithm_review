# 숨바꼭질
from collections import deque

n, k = map(int, input().split())

board = [-1] * 100001

q = deque()
q.append(n)
board[n] = 0

while q:
    now = q.popleft()
    if now == k:
        break
    for nxt in (now+1, now-1, now*2):
        if 0<=nxt<=100000 and board[nxt] == -1:
            q.append(nxt)
            board[nxt] = board[now] + 1

print(board[k])