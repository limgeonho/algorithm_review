# 벽 부수고 이동하기 2
# 벽 부수고 이동하기 1, 2, 말이 되고픈 원숭이 => 전부 단순한 BFS탐색 + 각각의 경우에 따른 분류가 필요함
# => 같은 형태의 BFS리스트가 경우에 따라 여러개로 생성된다
# 해당되는 상황에 맞는 리스트에 값을 계산
# 각각의 경우를 넘나들면서 리스트의 값이 갱신된다.

from collections import deque
import pprint
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                q.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
            if z+1 <= k and board[nx][ny] == 1 and visited[nx][ny][z+1] == 0:
                q.append((nx, ny, z+1))
                visited[nx][ny][z+1] = visited[x][y][z] + 1


# answer = []
# if visited[-1][-1] == [0] * (k+1):
#     print(-1)
# else:
#     for i in range(k+1):
#         if visited[-1][-1][i] != 0:
#             answer.append(visited[-1][-1][i])
#     print(min(answer))

for i in range(n):
    for j in range(m):
        print(visited[i][j][0], end=' ')
    print()

print('======================')

for i in range(n):
    for j in range(m):
        print(visited[i][j][1], end=' ')
    print()

print('======================')

for i in range(n):
    for j in range(m):
        print(visited[i][j][2], end=' ')
    print()

print('======================')