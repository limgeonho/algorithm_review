# 부등호
# 앞에서부터 순차적으로 순열

def check(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def go(L, z):
    global mx, mn
    if L == n+1:
        if not len(mn):
            mn = z
        else:
            mx = z
        return
    for i in range(10):
        if not visited[i]:
            if L == 0 or check(z[-1], str(i), array[L-1]):
                visited[i] = True
                go(L+1, z+str(i))
                visited[i] = False

n = int(input())
array = input().split()
mx = ''
mn = ''
visited = [False] * 10

go(0, '')

print(mx)
print(mn)

# def go(lev):
#     if lev == n + 1:
#         for i in range(len(arr)-1):
#             if possible(arr[i], arr[i + 1], sign[i]):
#                 continue
#             else:
#                 return
#         else:
#             answer.append(arr[:])
#         # for ~ else ~
#         return
#     for i in range(10):
#         if used[i] == 1:
#             continue
#         arr[lev] = i
#         used[i] = 1
#         go(lev + 1)
#         used[i] = 0
#
#
# def possible(i, j, k):
#     if k == "<":
#         return i < j
#     if k == ">":
#         return i > j
#     return True
#
#
# n = int(input())
# sign = list(map(str, input().split()))
# result = []
# used = [0] * 10
# arr = [0] * (n + 1)
#
# answer = []
#
# go(0)
#
# print(''.join(map(str, answer[-1])))
# print(''.join(map(str, answer[0])))