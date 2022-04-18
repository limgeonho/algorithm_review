import heapq

def dijkstra(start, distance, graph):
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
                
        
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    
    distance = [2147000000] * (N+1)
    dijkstra(1, distance, graph)
    
    for i in range(1, len(distance)):
        if distance[i] <= K:
            answer += 1

    return answer