def subset(L, ss):
    if L == n:
        print(*ss)
        return
    subset(L+1, ss + [arr[L]])
    subset(L+1, ss)

n = int(input())
arr = list(range(1, n+1))

subset(0, [])