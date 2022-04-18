from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, visited, board):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board[0]) and visited[nx][ny] == -1 and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[now_x][now_y] + 1

def solution(maps):
    answer = 0
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    bfs(0, 0, visited, maps)
    answer = visited[-1][-1]
    
    return answer