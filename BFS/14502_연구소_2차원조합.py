# 연구소 2차원 조합
# 조합 + 브루트 포스 + bfs
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(tmp):
    q = deque()
    # 바이러스 시작점 찾기
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))
    print(q)
    # 바이러스 뿌리기
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] == 0:
                q.append((nx, ny))
                tmp[nx][ny] = 2
    # 안전 영역 카운팅
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1

    return cnt


def comb(L, start):
    global answer
    if L == 3:
        # 똑같은 형태의 임시 2차원 리스트를 생성
        tmp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][j]

        # 조합으로 뽑힌 것을 2차원 좌표 값으로 계산해줌
        for j in res:
            x = j // m
            y = j % m
            # 벽을 세울수 없는 곳이면 return(백트래킹)
            if tmp[x][y] != 0:
                return
            # 벽을 세움
            tmp[x][y] = 1

        # 벽을 세운 곳을 가지고 check => 안전영역 개수 return
        safe = check(tmp)

        # 최대값 갱신
        if answer < safe:
            answer = safe
        return

    for i in range(start, m*n):
        res[L] = i
        comb(L+1, i+1)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0
res = [0] * 3
comb(0, 0)
print(answer)