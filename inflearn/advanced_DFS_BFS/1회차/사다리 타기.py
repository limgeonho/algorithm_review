def dfs(x, y):
    visited[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1] == 1 and visited[x][y-1] == 0:
            dfs(x, y-1)
        elif y+1<10 and board[x][y+1] == 1 and visited[x][y+1] == 0:
            dfs(x, y+1)
        else:
            dfs(x-1, y)

board = []
for _ in range(10):
    board.append(list(map(int, input().split())))

visited = [[0] * 10 for _ in range(10)]

for i in range(10):
    if board[9][i] == 2:
        dfs(9, i)