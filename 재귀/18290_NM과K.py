# NM과 K
# 2차원 리스트의 조합을 1차원으로 만들어서 사용...

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# def go(L, start, total):
#     global answer
#     if L == k:
#         if total > answer:
#             answer = total
#         return
#     # 2차원을 1차원으로...
#     for i in range(start, m*n):
#         x = i//m
#         y = i%m
#
#         if visited[x][y]:
#             continue
#
#         flag = True
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0<=nx<n and 0<=ny<m:
#                 if visited[nx][ny]:
#                     flag = False
#         if flag:
#             visited[x][y] = True
#             go(L+1, i+1, total + array[x][y])
#             visited[x][y] = False

def go(L, start, total):
    global answer
    if L == k:
        if total > answer:
            answer = total
        return

    for i in range(start, n*m):
        x = i // m
        y = i % m

        if visited[x][y]:
            continue
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]:
                    break
        else:
            visited[x][y] = True
            go(L+1, i+1, total + array[x][y])
            visited[x][y] = False

n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
answer = -2147000000
res = [0] * k
visited = [[False]*m for _ in range(n)]

go(0, 0, 0)

print(answer)