def subset(L, total, totalTime):
    global res
    if totalTime > m:
        return
    if L == n:
        if total > res:
            res = total
        return
    else:
        subset(L+1, total + s[L], totalTime + t[L])
        subset(L+1, total, totalTime)

n, m = map(int, input().split())
res = -2147000000
s = []
t = []
for _ in range(n):
    score, time = map(int, input().split())
    s.append(score)
    t.append(time)

subset(0, 0, 0)
print(res)