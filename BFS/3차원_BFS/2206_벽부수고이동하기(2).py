# 벽 부수고 이동하기(2)
# 3차원 리스트를 활용하는 문제
# 하나의 2차원 리스트를 가지고 활용하는 것이 아닌 2차원 리스트의 상황에 따라
# 다양한 2차원 리스트의 모양이 필요하기 때문에 => 3차원 리스트로
# 3차원 리스트는 2차원 리스트를 여러개 만든 것임 => 각각의 상황에 따라 다르게 생성

from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1

    while q:
        a, b, c = q.popleft()
        for v in visited:
            print(v)
        print()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0<=nx<n and 0<=ny<m:
                # 길을 만난 경우
                # 벽을 뚫고 왔다면 벽을 뚫고 온 리스트에 / 벽을 뚫지 않았다면 뚫지 않은 리스트에
                if board[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    q.append((nx, ny, c))
                    visited[nx][ny][c] = visited[a][b][c] + 1
                # 벽을 만난 경우
                # 아직까지 벽을 뚫은 적이 없다면 뚫고 뚫은 리스트에
                if c == 0 and board[nx][ny] == 1 and visited[nx][ny][c+1] == 0:
                    q.append((nx, ny, c+1))
                    visited[nx][ny][c+1] = visited[a][b][c] + 1


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
bfs(0, 0, 0)

if visited[-1][-1][0] != 0 and visited[-1][-1][1] != 0:
    print(min(visited[-1][-1][0], visited[-1][-1][1]))
elif visited[-1][-1][0] != 0:
    print(visited[-1][-1][0])
elif visited[-1][-1][1] != 0:
    print(visited[-1][-1][1])
else:
    print(-1)
