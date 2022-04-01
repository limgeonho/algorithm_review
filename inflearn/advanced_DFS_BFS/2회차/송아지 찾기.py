from collections import deque

s, e = map(int, input().split())
visited = [-1] * 10001

q = deque()
q.append(s)

visited[s] = 0

while q:
    now = q.popleft()
    if now == e:
        break
    for nxt in (now+1, now-1, now+5):
        if 1 <= nxt <= 10000 and visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            q.append(nxt)

print(visited[e])