def solution(board):
    answer = -2147000000
    
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0:
            return 0
        return 1
      
    tmp = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp += board[i][j]
    if tmp == 0:
        return 0
        
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                if answer < board[i][j]:
                    answer = board[i][j]

    return answer**2