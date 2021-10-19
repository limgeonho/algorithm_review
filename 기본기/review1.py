n = int(input())
array = list(map(int, input().split()))

visited = [False] * len(array)
res = [0] * n

def perm(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = array[i]
        perm(L+1)
        visited[i] = False

# perm(0)


def perm_with(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        res[L] = array[i]
        perm_with(L+1)

# perm_with(0)

def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        comb(L+1, i+1)

# comb(0, 0)

# ====================================
# 부분집합

def powerset(L, ps):
    if L == n:
        if not ps:
            return
        print(ps)
        return
    powerset(L+1, ps + [array[L]])
    powerset(L+1, ps)

powerset(0, [])


