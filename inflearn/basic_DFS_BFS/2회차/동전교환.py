def perm_with(L, total):
    global res
    if L >= res:
        return
    if total > m:
        return
    if total == m:
        if L < res:
            res = L
            return
    else:
        for i in range(len(arr)):
            perm_with(L+1, total + arr[i])

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort(reverse=True)
res = 2147000000

perm_with(0, 0)
print(res)