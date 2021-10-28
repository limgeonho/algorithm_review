# 연구소3
# 조합 + bfs의 visited 이동 횟수 누적
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(res, tmp, visited):
    print('========================')
    q = deque()
    # 시작 바이러스를 q에 넣고 tmp리스트에 세팅 + visited에도 시작점으로 0설정
    need_to_activate = []
    for v in virus:
        if v in res:
            q.append(v)
            tmp[v[0]][v[1]] = 2
            visited[v[0]][v[1]] = 0
        else:
            need_to_activate.append((v[0], v[1]))
    # 일반적인 bfs 채우기 과정
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and tmp[nx][ny] == 0 and visited[nx][ny] == -1:
                if (nx, ny) in need_to_activate:
                    tmp[nx][ny] = 2
                    visited[nx][ny] = visited[x][y]
                    need_to_activate.remove((nx, ny))
                    q.append((nx, ny))
                    continue
                tmp[nx][ny] = 2
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    print(visited)
    print(need_to_activate)
    if need_to_activate:
        return 2147000000
    # 이동하지 않은 곳이 있다면 그냥 최대값 return
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 0:
                return 2147000000

    # 이동하지 않은 곳이 없다면 그 안에서 최대값 return
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] > cnt:
                cnt = visited[i][j]

    return cnt


# 전체 바이러스 리스트에서 원하는 개수만큼 조합으로 추출
def comb(L, start):
    global answer
    # 원하는 개수만큼 뽑고 => tmp에 board 복사 + visited리스트 생성
    if L == m:
        tmp = [[0] * n for _ in range(n)]
        visited = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 벽만 복사 => 시작 바이러스는 나중에 추가
                if board[i][j] == 1:
                    tmp[i][j] = board[i][j]
        temp = check(res, tmp, visited)
        # 전체 조합의 경우의 수로 만들어진 리스트의 값 중 최소값으로 갱신
        if temp < answer:
            answer = temp
        return

    for i in range(start, len(virus)):
        res[L][0] = virus[i][0]
        res[L][1] = virus[i][1]
        comb(L+1, i+1)


# 바이러스가 있는 위치를 전부 하나의 리스트에 담음 => 나중에 조합으로 원하는 개수 만큼 뽑기
def find_virus(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.append([i, j])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
res = [[0, 0] for _ in range(m)]
answer = 2147000000
virus = []

find_virus(board)

comb(0, 0)

if answer == 2147000000:
    print(-1)
else:
    print(answer)