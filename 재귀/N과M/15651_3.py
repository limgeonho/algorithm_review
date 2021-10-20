# N과 M(3)

def go(L):
    if L == m:
        print(*res)
        return
    for i in range(n):
        res[L] = i+1
        go(L+1)

n, m = map(int, input().split())
res = [0] * m
go(0)