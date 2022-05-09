# 해당 문제는 단순하게 로직 구현만 생각한다면 매우 쉽지만 
# 당연히~ 시간초과!!! 
# => 모든 쿼리를 하나씩 전체 2차원 리스트를 순회하면서 값을 수정하는 방법은 적절하지 않다(시간이 매우 오래 걸림)
# 해결책 : 누적합을 이용하자!!(imos 기법!)
# imos방법은 2차원 리스트에서 원하는 구역에 추가할 값을 해당 시작점과 끝점에만 표시를 전부 다 수행하고
# 마지막에 최종적으로 전체 2차원 리스트를 돌면서 누적합을 구하는 방법임
# 따라서 (시작점, 끝점) 표시만 하고 전체 2차원 리스트는 1번만 순회하면 전체 쿼리를 실행한 결과를 알 수 있다.
def attack(board, skill):
    for i in range(skill[1], skill[3]+1):
        for j in range(skill[2], skill[4]+1):
            board[i][j] -= skill[5]
    return board

def defense(board, skill):
    for i in range(skill[1], skill[3]+1):
        for j in range(skill[2], skill[4]+1):
            board[i][j] += skill[5]
    return board


def solution(board, skills):
    answer = 0
    for skill in skills:
        if skill[0] == 1:
            board = attack(board, skill)
        else:
            board = defense(board, skill)
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer
  
#####################################################################################
# imos 기법을 활용한 방법

def imos(changed, skills):
    for skill in skills:
        r1 = skill[1]
        c1 = skill[2]
        r2 = skill[3]
        c2 = skill[4]
        degree = skill[5]
    
    # ======== imos ======== 
        if skill[0] == 1:
            changed[r1][c1] -= degree
            changed[r1][c2+1] += degree
            changed[r2+1][c1] += degree
            changed[r2+1][c2+1] -= degree
        else:
            changed[r1][c1] += degree
            changed[r1][c2+1] -= degree
            changed[r2+1][c1] -= degree
            changed[r2+1][c2+1] += degree
    
    # 행 sweep
    for r in range(n+1):
        for c in range(1, m+1):
            changed[r][c] += changed[r][c-1]
    
    # 열 sweep
    for c in range(m+1):
        for r in range(1, n+1):
            changed[r][c] += changed[r-1][c]
    
    # ======================
    return
            
def solution(board, skills):
    answer = 0
    global n, m
    n = len(board)
    m = len(board[0])

    changed = [[0] * (m+1) for _ in range(n+1)]
    imos(changed, skills)
    
    for r in range(n):
        for c in range(m):
            if board[r][c] + changed[r][c] > 0:
                answer += 1
    return answer