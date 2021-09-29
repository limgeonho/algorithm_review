# 숨바꼭질

import heapq
import sys
INF = sys.maxsize

n, m = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            if distance[now] < dist:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
answer = []
max_num = max(distance[1:])
answer.append(distance.index(max_num))
answer.append(max_num)
answer.append(distance.count(max_num))
print(*answer)