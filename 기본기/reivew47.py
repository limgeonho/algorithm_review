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
################################################################
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
################################################################
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
# def union_parent(parent,a ,b):
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
#         cnt += 1
#         result += cost
# if cnt == v-1:
#     print('MST')
# else:
#     print(-1)
################################################################
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
################################################################
# import heapq
# import sys
# INF = sys.maxsize
# n, m = map(int, input().split())
# start = int(input())
# graph = [[]for _ in range(n+1)]
# distance = [INF] * (n+1)
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
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
# dijkstra(start)
################################################################
# import sys
# INF = sys.maxsize
# n, m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
# for i in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
################################################################
# n, limit = map(int, input().split())
# dp = [0] * (limit+1)
# for i in range(n):
#     weight, value = map(int, input().split())
#     for j in range(limit, weight-1, -1):
#         dp[j] = max(dp[j], dp[j-weight] + value)
# print(max(dp))
################################################################
# n, limit = map(int, input().split())
# dp = [0] * (limit+1)
# for i in range(n):
#     weight, value = map(int, input().split())
#     for j in range(weight, limit+1):
#         dp[j] = max(dp[j], dp[j-weight] + value)
# print(max(dp))
################################################################
# array = [3, 1, 2, 4, 8, 6, 7]
# n = len(array)
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if array[j] < array[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
################################################################
# from bisect import bisect_left
# array = [3, 1, 2, 4, 8, 6, 7]
# dp = [array[0]]
# for i in range(1, n):
#     if dp[-1] < array[i]:
#         dp.append(array[i])
#     else:
#         dp[bisect_left(dp, array[i])] = array[i]
# result = max(dp)
################################################################
# array = [3, 1, 2, 4, 8, 6, 7]
# n = len(array)
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if dp[j] < dp[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# order = max(dp)
# answer = []
# for i in range(n-1, -1, -1):
#     if dp[i] == order:
#         answer.append(array[i])
#         order -= 1
# print(answer[::-1])
################################################################
# word_1 = input()
# word_2 = input()
#
# n = len(word_1)
# m = len(word_2)
#
# word_1 = ' ' + word_1
# word_2 = ' ' + word_2
#
# dp = [[0] * (m+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if word_1[i] == word_2[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[n][m])
################################################################
# def rotate(array):
#     row = len(array)
#     col = len(array[0])
#
#     res = [[0] * row for _ in range(col)]
#
#     for r in range(row):
#         for c in range(col):
#             res[c][row-r-1] = array[r][c]
#     return res
################################################################
# array = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# array = list(zip(*array))
# print(array)
################################################################
# def rotate(array):
#     changed = [k[::-1] for k in zip(*array)]
#     return changed
################################################################
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     left = []
#     right = []
#     pivot = array[0]
#     for i in range(1, len(array)):
#         if array[i] < pivot:
#             left.append(array[i])
#         else:
#             right.append(array[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
################################################################
# def solution(n, q):
#     base = ''
#     while n > 0:
#         n, mod = divmod(n, q)
#         base += str(mod)
#     return base[::-1]
################################################################
# def is_prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             return False
#     else:
#         return True
################################################################
# n = 1000
# array = [True for i in range(n+1)]
#
# for i in range(2, int(n**0.5)+1):
#     if array[i]:
#         j = 2
#         while i * j <= n:
#             array[i * j] = False
#             j += 1
# for i in range(2, n+1):
#     if array[i]:
#         print(i, end=' ')
################################################################
# n, m = 5
# data = [1, 2, 3, 4, 5]
#
# cnt = 0
# interval_sum = 0
# end = 0
#
# for start in range(n):
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     if interval_sum == m:
#         cnt += 1
#     interval_sum -= data[start]
# print(cnt)
################################################################
# array = [1, 2, 3]
# n = len(array)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(array[j], end=' ')
#     print()
################################################################