# 돌 그룹
# 2차원 리스트에 사용한 값을 표시
# 처리해야하는 값이 3개이기 때문에 3 -(선택한 두개의 값) = 나머지 하나의 값(2차원 리스트 활용)

from collections import deque


def bfs():
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        z = total - x - y
        if x == y == z:
            print(1)
            return
        # 가능한 조합을 전부 뽑아서 해보기
        for A, B in (x, y), (x, z), (y, z):
            if A < B:
                B -= A
                A += A
            elif A > B:
                A -= B
                B += B
            else:
                continue

            C = total - A - B
            X = min(A, B, C)
            Y = max(A, B, C)
            if not visited[X][Y]:
                q.append((X, Y))
                visited[X][Y] = True
    print(0)


a, b, c = map(int, input().split())
total = a + b + c
visited = [[False] * total for _ in range(total)]

if total % 3:
    print(0)
else:
    bfs()
