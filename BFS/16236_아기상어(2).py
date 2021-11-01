# 아기 상어(2)
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(board, x, y, size):
    ans = []
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                # 갈 수 있는지, 먹을 수 있는지 flag 초기화
                go = False
                eat = False
                if board[nx][ny] == 0:
                    go = True
                elif board[nx][ny] < size:
                    go = True
                    eat = True
                elif board[nx][ny] == size:
                    go = True

                if go:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx, ny))
                    if eat:
                        ans.append((visited[nx][ny], nx, ny))
    # 더 이상 먹을 수 없음
    if not ans:
        return None
    # 거리가 짧은 순으로 정렬
    ans.sort()
    # 가장 가까운 거리의 먹이정보 return
    return ans[0]


def find_shark(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                return i, j

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 상어 찾기
x, y = find_shark(board)
# 상어 위치 0 으로 세팅
board[x][y] = 0

answer = 0
size = 2
exp = 0

while True:
    # 이동 거리, 현재 위치 return
    tmp = bfs(board, x, y, size)

    if tmp is None:
        break
    dist, nx, ny = tmp

    # 상어가 온 위치 = 0 으로 세팅
    board[nx][ny] = 0
    # 거리 누적
    answer += dist
    # 1마리 먹은거니까 경험치 +1
    exp += 1
    # 사이즈와 경험치가 같으면 사이즈 업 +1
    if size == exp:
        size += 1
        exp = 0
    # 상어가 온 위치를 현 위치로 세팅
    x, y = nx, ny

print(answer)