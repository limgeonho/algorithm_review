from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
for _ in range(7):
    tmp = list(map(int, input().split(' ')))
    arr.append(tmp)

visited = [[0] * 7 for _ in range(7)]
visited[0][0] = 0
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    if x == 6 and y == 6:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<7 and 0<=ny<7 and not visited[nx][ny] and arr[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

if visited[-1][-1]:
    print(visited[-1][-1])
else:
    print(-1)