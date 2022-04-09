def solution(s):
    answer = ''
    for word in s.split():
        tmp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        answer += tmp
        answer += ' '
    return answer[:-1]