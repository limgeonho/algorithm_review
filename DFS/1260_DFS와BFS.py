# DFS와 BFS
from collections import deque

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


dfs(start)

visited = [False] * (n+1)
print()

bfs(start)