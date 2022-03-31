def subset(L, ss, ts):
    global res
    if res > total - ts + ss:
        return
    if ss > limit:
        return
    if L == n:
        if ss > res:
            res = ss
            return
    else:
        subset(L+1, ss + arr[L], ts + arr[L])
        subset(L+1, ss, ts + arr[L])


limit, n = map(int, input().split())
arr = []
res = -2147000000
for _ in range(n):
    arr.append(int(input()))
total = sum(arr)
subset(0, 0, 0)
print(res)