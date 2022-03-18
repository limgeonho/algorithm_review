# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# cnt = 0
# arr.sort(reverse=True)
#
# while True:
#     if m == 0:
#         break
#     for a in arr:
#         if m % a == 0:
#             tmp = m // a
#             cnt += tmp
#             m = m - (tmp * a)
#         else:
#             continue
#
# print(cnt)

def dfs(L, total):
    global res
    if L >= res:
        return

    if total > m:
        return

    if total == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            dfs(L+1, total + arr[i])

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

res = 2147000000
arr.sort(reverse=True)

dfs(0, 0)
print(res)