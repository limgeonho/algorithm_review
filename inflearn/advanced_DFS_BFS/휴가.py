def subset(L, P):
    global res
    if L > n:
        return
    if L == n:
        if P > res:
            res = P
            return
    else:
        subset(L+time[L], P+pay[L])
        subset(L+1, P)


n = int(input())
time = []
pay = []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

res = -2147000000

subset(0, 0)
print(res)