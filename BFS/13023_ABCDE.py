# ABCDE

def dfs(start, cnt):
    global answer
    if cnt == 5:
        answer = True
        return
    visited[start] = True
    for i in relation[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


n, m = map(int, input().split())
relation = [[] for _ in range(n)]
visited = [False] * n
answer = False

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)


for i in range(n):
    dfs(i, 1)
    visited[i] = False
    if answer:
        print(1)
        break
else:
    print(0)
