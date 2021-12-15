# n = int(input())
# array = list(map(int, input().split()))
# res = [0] * n
# visited = [False] * len(array)
#
# def perm(L):
#     if L == n:
#         print(*res)
#         return
#     for i in range(len(array)):
#         if visited[i]:
#             continue
#         visited[i] = True
#         res[L] = array[i]
#         perm(L+1)
#         visited[i] = False
# perm(0)
#
# def comb(L, start):
#     if L == n:
#         print(*res)
#         return
#     for i in range(start, len(array)):
#         res[L] = array[i]
#         comb(L+1, i+1)
# comb(0, 0)
#
# def perm_with(L):
#     if L == n:
#         print(*res)
#         return
#     for i in range(len(array)):
#         res[L] = array[i]
#         perm_with(L+1)
# perm_with(0)
#
# def subset(L, ss):
#     if L == n:
#         print(*ss)
#         return
#     subset(L+1, ss + [array[L]])
#     subset(L+1, ss)
# subset(0, [])
#
# def next_perm(array):
#     i = len(array) - 1
#     while i > 0 and array[i-1] >= array[i]:
#         i -= 1
#     if i <= 0:
#         return False
#     j = len(array) - 1
#     while array[i-1] >= array[j]:
#         j -= 1
#     array[i-1], array[j] = array[j], array[i-1]
#     j = len(array) - 1
#     while i < j:
#         array[i], array[j] = array[j], array[i]
#         i += 1
#         j -= 1
#     return True
########################################################
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
# v, e = map(int, input().split())
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i
# for _ in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
########################################################
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
# v, e = map(int, input().split())
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i
# edges = []
# result = 0
# cnt = 0
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
# edges.sort()
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         cnt += 1
# if cnt == v-1:
#     print('MST')
# else:
#     print(-1)
########################################################
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
########################################################
# import heapq
# import sys
# INF = sys.maxsize
# n, m = map(int, input().split())
# start = int(input())
# graph = [[]for _ in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = i[1] + dist
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
# dijkstra(start)
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
