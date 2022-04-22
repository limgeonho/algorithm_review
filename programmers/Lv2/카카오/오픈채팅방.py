def solution(record):
    answer = []
    names = {}
    for rc in record:
        tmp = rc.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            names[tmp[1]] = tmp[2]
    
    for rc in record:
        tmp = rc.split()
        if tmp[0] == 'Enter':
            answer.append(names[tmp[1]] + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(names[tmp[1]] + '님이 나갔습니다.')
        else:
            pass
    return answer