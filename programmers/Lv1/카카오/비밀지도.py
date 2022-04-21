
def solution(n, arr1, arr2):
    answer = []
    board1 = [0] * n
    board2 = [0] * n
    board3 = [[''] * n for _ in range(n)]
    
    for i in range(n):
        board1[i] = str(bin(arr1[i])[2:]).rjust(n, '0')
    
    for i in range(n):
        board2[i] = str(bin(arr2[i])[2:]).rjust(n, '0')
            
    for i in range(n):
        for j in range(n):
            if board1[i][j] == '1' or board2[i][j] == '1' :
                board3[i][j] = '#'
            else:
                board3[i][j] = ' '
    
    for i in range(n):
        board3[i] = ''.join(board3[i])
    answer = board3
    
    return answer