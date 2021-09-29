# 골목 대장 호석 - 기능성
# 틀림 ㅜ
import heapq
import sys
INF = sys.maxsize

n, m, s, e, c = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

pay = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    pay.append(cost)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

pay.sort()
dijkstra(s)

money = distance[e]
if c > money:
    print(pay[-2])
elif c == money:
    print(pay[-1])
else:
    print(-1)