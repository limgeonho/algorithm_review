def subset(L, total, value):
    global res
    if L == len(arr):
        if total > m:
            return
        else:
            if value > res:
                res = value
                return
    else:
        subset(L+1, total + arr[L][1], value + arr[L][0])
        subset(L+1, total, value)

n, m = map(int, input().split())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

res = -2147000000

subset(0, 0, 0)

print(res)