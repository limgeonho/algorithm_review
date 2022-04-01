def subset(L, pay):
    global res
    if L > n:
        return
    if L == n:
        if pay > res:
            res = pay
        return
    else:
        subset(L+tt[L], pay+pp[L])
        subset(L+1, pay)

n = int(input())
tt = []
pp = []
res = -2147000000
for _ in range(n):
    t, p = map(int, input().split())
    tt.append(t)
    pp.append(p)

subset(0, 0)
print(res)