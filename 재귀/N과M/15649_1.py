# N과 M(1)

def go(L):
    if L == m:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = i+1
        go(L+1)
        visited[i] = False

n, m = map(int, input().split())

visited = [False] * n
res = [0] * m

go(0)