n = int(input())
arr = list(map(int, input().split()))
res = [0] * n
visited = [False] * len(arr)

def perm(L):
    if L == n:
        print(*res)
        return
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = arr[i]
        perm(L+1)
        visited[i] = False

# perm(0)

def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(arr)):
        res[L] = arr[i]
        comb(L+1, i+1)

# comb(0, 0)

def perm_with(L):
    if L == n:
        print(*res)
        return
    for i in range(len(arr)):
        res[L] = arr[i]
        perm_with(L+1)

# perm_with(0)

def subset(L, ss):
    if L == n:
        print(*ss)
        return
    subset(L+1, ss + [arr[L]])
    subset(L+1, ss)

subset(0, [])