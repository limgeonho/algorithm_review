
def subset(L, ss):
    if L == n:
        print(*ss)
        return
    subset(L+1, ss+ [array[L]])
    subset(L+1, ss)


n = int(input())
array = range(1, n+1)
subset(0, [])

