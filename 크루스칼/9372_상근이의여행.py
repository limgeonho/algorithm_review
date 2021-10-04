# 상근이의 여행


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


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    countries = [0] * (n+1)
    for i in range(1, n+1):
        countries[i] = i

    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(countries, a) != find_parent(countries, b):
            union_parent(countries, a, b)
            cnt += 1

    print(cnt)