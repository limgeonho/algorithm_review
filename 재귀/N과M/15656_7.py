# N과 M(7)

def go(L):
    if L == m:
        print(*res)
        return
    for i in range(n):
        res[L] = array[i]
        go(L+1)


n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
res = [0] * m

go(0)