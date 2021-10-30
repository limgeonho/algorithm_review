# 움직이는 미로 탈출
# 한 번 움직일 때 마다 board가 내려온다(한 칸씩)
# from collections import deque
#
# dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

# def bfs(a, b, c):
#     q = deque()
#     q.append((a, b, c))
#
#     while q:
#         x, y, turn = q.popleft()
#         for k in range(9):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             # 현재 위치에 벽이 있는지? / 움직인 다음에 이동한 자리로 벽이 내려오는지?
#             if 0<=nx<8 and 0<=ny<8 and not board[nx-turn][ny] == '#' and not board[nx-turn-1][ny] == '#':
#                 if nx - turn < 0:
#                     return 1
#                 q.append((nx, ny, turn+1))
#     return 0
#
#
# board = [list(map(str, input())) for _ in range(8)]
# print(bfs(7, 0, 0))

from collections import deque

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        # 벽이 이동해 버리면 아예 새로운 visited리스트를 만들어 준다 => 지도가 달라졌으니까!!
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            x, y = q.popleft()
            print(x, y)
            if x == 0 and y == 7:
                return 1

            if board[x][y] == '#':
                continue

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<8 and 0<=ny<8 and board[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        # 행을 내리는 방법 => 마지막 줄 pop() => 맨 위에 insert(idx, content)
        board.pop()
        board.insert(0, ['.']*8)

    return 0


board = [list(map(str, input())) for _ in range(8)]

print(bfs(7, 0))