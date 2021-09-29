# 지름길

n, d = map(int, input().split())

shortcut = [list(map(int, input().split())) for _ in range(n)]
distance = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for start, end, dist in shortcut:
        if i == start and end <= d and distance[start] + dist <= distance[end]:
            distance[end] = distance[start] + dist

print(distance[d])