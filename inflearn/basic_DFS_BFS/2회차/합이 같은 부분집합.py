def subset(L, ss):
    global flag
    if sum(ss) > total // 2:
        return
    if L == n:
        if sum(ss) * 2 == total:
            flag = True
            return
        else:
            return

    subset(L+1, ss + [arr[L]])
    subset(L+1, ss)

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
flag = False
subset(0, [])

if flag:
    print("YES")
else:
    print("NO")