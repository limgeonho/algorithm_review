# 백도어

import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if array[i[0]] == 1:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
array = list(map(int, input().split()))
array[-1] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

dijkstra(0)

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])

