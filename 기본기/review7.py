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
#
# # perm(0)
#
# def comb(L, start):
#     if L == n:
#         print(*res)
#         return
#     for i in range(start, len(array)):
#         res[L] = array[i]
#         comb(L+1, i+1)
#
# # comb(0, 0)
#
# def perm_with(L):
#     if L == n:
#         print(*res)
#         return
#     for i in range(len(array)):
#         res[L] = array[i]
#         perm_with(L+1)
#
# # perm_with(0)
#
# n = int(input())
# array = list(map(int, input().split()))
# def subset(L, ss):
#     if L == n:
#         if not ss:
#             return
#         print(ss)
#         return
#     subset(L+1, ss + [array[L]])
#     subset(L+1, ss)
#
# subset(0, [])


array = list(map(int, input().split()))
def next_perm(arr):
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[i-1] >= arr[j]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True

if next_perm(array):
    print(array)
else:
    print(-1)