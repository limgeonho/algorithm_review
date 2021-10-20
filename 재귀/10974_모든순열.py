# 모든 순열

def go(L):
    if L == n:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = i+1
        go(L+1)
        visited[i] = False

n = int(input())
visited = [False] * n
res = [0] * n

go(0)