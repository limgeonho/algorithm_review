# N과 M(2)

def go(L, start):
    if L == m:
        print(*res)
        return
    for i in range(start, n):
        res[L] = i+1
        go(L+1, i+1)

n, m = map(int, input().split())
res = [0] * m

go(0, 0)
