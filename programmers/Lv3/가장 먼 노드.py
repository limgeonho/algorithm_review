# 그냥 단순하게 BFS로도 풀 수 있는 문제를.. 굳이 다익스트라로?ㅋㅋㅋ
# 아마 출발점이 1 하나 밖에 없어서 그런듯..!!

import heapq

def dijkstra(n, edge, start):
    distance = [2147000000] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for ed in edge:
        graph[ed[0]].append((ed[1], 1))
        graph[ed[1]].append((ed[0], 1))
    
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
                heapq.heappush(q, (cost, i[0]))
    return distance
    
    
def solution(n, edge):
    answer = 0
    result = dijkstra(n, edge, 1)
    result = result[1:]
    maxNum = max(result)
    for res in result:
        if res == maxNum:
            answer += 1
    
    return answer