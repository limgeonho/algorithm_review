# 스타트링크
# 방문여부 먼저 체크하기 무조건!!!

from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [-1] * (f+1)
q = deque()
q.append(s)
visited[s] = 0

while q:
    now = q.popleft()
    if now == g:
        break
    for nx in (now+u, now-d):
        if 1<=nx<=f and visited[nx] == -1:
            visited[nx] = visited[now] + 1
            q.append(nx)

if visited[g] != -1:
    print(visited[g])
else:
    print('use the stairs')

