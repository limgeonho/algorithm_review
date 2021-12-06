n = int(input())
array = list(map(int, input().split()))
res = [0] * n
visited = [False] * len(array)

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

perm(0)
print('==========================')

def comb(L, start):
    if L == n:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        comb(L+1, i+1)

comb(0, 0)
print('==========================')


def perm_with(L):
    if L == n:
        print(*res)
        return
    for i in range(len(array)):
        res[L] = array[i]
        perm_with(L+1)

perm_with(0)
print('==========================')

def subset(L, ss):
    if L == n:
        print(ss)
        return
    subset(L+1, ss + [array[L]])
    subset(L+1, ss)

subset(0, [])
print('==========================')

