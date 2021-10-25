# 연결 요소의 개수
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n, m = map(int, input().split())
# answer = set()
#
# parent = [0] * (n+1)
# for i in range(n+1):
#     parent[i] = i
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# for i in range(1, n+1):
#     answer.add(find_parent(parent, parent[i]))
#
# print(len(answer))

def dfs(x):
    visited[x] = True
    for i in relation[x]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
visited = [False] * (n+1)
relation = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)