def solution(phone_number):
    answer = ''
    tmp = len(phone_number)-4
    answer = '*' * (tmp) + phone_number[tmp:]
    return answer