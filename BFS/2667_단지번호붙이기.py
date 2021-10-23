# 단지번호 붙이기
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    array[x][y] = '0'

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and array[nx][ny] == '1':
                q.append((nx, ny))
                array[nx][ny] = '0'
                cnt += 1

    return cnt


n = int(input())
array = [list(input()) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if array[i][j] == '1':
            cnt = 1
            cnt = bfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)