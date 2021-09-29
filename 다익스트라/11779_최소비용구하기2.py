# 최소비용 구하기 2


import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
trace = [0] * (n + 1)

# 간선 정보 입력(연결리스트)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                trace[i[0]] = now
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

path = [end]
tmp = trace[end]
while True:
    if tmp == 0:
        break
    path.append(tmp)
    tmp = trace[tmp]

print(distance[end])
print(len(path))
print(*path[::-1])