from itertools import combinations
from collections import deque

def bfs(start, visited, board):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 1
    while q:
        now = q.popleft()
        for i in board[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 2147000000
    for comb in combinations(wires, n-2):
        board = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        temp = []
        for com in comb:
            board[com[0]].append(com[1])
            board[com[1]].append(com[0])
        for i in range(1, n+1):
            if not visited[i]:
                tmp = bfs(i, visited, board)
                temp.append(tmp)
        if answer > abs(temp[0] - temp[1]):
            answer = abs(temp[0] - temp[1])
        
    return answer