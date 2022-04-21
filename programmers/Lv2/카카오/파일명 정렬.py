# 3개의 덩어리로 나누는 방법 if elif else~ 이용
# sort()는 여러개의 조건을 넣을 수 있음

def solution(files):
    answer = []
    sliced = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                check = True
            elif not check:
                head += file[i]
            else:
                tail = file[i:]
                break
                  
        sliced.append((head, number, tail))
    sliced.sort(key=lambda x:(x[0].upper(), int(x[1])))
    for sl in sliced:
        answer.append(''.join(sl))
    return answer