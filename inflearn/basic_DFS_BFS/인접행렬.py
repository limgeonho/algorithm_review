n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end=' ')
    print()

