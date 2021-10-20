# N과 M(6)

def go(L, start):
    if L == m:
        print(*res)
        return
    for i in range(start, n):
        res[L] = array[i]
        go(L+1, i+1)


n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
res = [0] * m

go(0, 0)