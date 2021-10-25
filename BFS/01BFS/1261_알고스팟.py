# 알고스팟
# 0-1 BFS 문제임...
# 0으로 가는 것은 가중치가 0
# 1로 가는 것은 가중치가 1
# => 따라서, bfs인데 가중치가 다르다? => 우선순위가 생김?
# => appendleft() - 가중치0 / append() - 가중치1
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                if board[nx][ny] == 0:
                    visited[nx][ny] = visited[now_x][now_y]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx, ny))



m, n = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

bfs(0, 0)


# print(visited)
print(visited[-1][-1])
