def countZero(x):
    tmp = 0
    tmp = x.count('0')
    return tmp

def change(x):
    tmp = 0
    tmp = x.count('1')
    temp = str(bin(tmp)[2:])
    return temp

def solution(s):
    answer = []
    zCnt = 0
    cnt = 0
    while s != '1':
        zCnt += countZero(s)
        s = change(s)
        cnt += 1
    
    answer = [cnt, zCnt]
    return answer