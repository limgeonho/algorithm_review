# 이분 그래프
from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    color[x] = 1
    while q:
        a = q.popleft()
        for i in relation[a]:
            if color[i] == 0:
                color[i] = -color[a]
                q.append(i)
            else:
                if color[i] == color[a]:
                    return False
    return True


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    relation = [[] for _ in range(n+1)]
    color = [0] * (n+1)
    answer = False

    for _ in range(m):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    for i in range(1, n+1):
        if not color[i]:
            tmp = bfs(i)
            if not tmp:
                answer = True
                break

    if not answer:
        print('YES')
    else:
        print('NO')