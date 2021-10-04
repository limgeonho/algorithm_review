# Bad Cowtractors
# MST를 만족시키지 않는 경우의 문제
# MST를 만족한다는 것은 MST의 경로의 개수 == 노드 -1 !!!!!!

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [-1] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=True)

res = 0
cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        cnt += 1

if cnt == n-1:
    print(res)
else:
    print(-1)
