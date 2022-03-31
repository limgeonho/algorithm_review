n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()


