# N과 M(5)

def go(L):
    if L == m:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = array[i]
        go(L+1)
        visited[i] = False

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

visited = [False] * n
res = [0] * m

go(0)