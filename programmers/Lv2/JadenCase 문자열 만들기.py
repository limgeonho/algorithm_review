def solution(s):
    answer = ''
    for word in (s.split(' ')):
        answer += word.capitalize()
        answer += ' '
    return answer[:-1]