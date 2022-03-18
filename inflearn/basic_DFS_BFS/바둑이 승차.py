
def subset(L, ss, ts):
    global res
    if ss > c:
        return
    if res > total - ts + ss:
        return

    if L == n:
        if ss > res:
            res = ss
            return
    else:
        subset(L+1, ss+arr[L], ts+arr[L])
        subset(L+1, ss, ts+arr[L])


c, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

total = sum(arr)

res = -2147000000
subset(0, 0, 0)
print(res)