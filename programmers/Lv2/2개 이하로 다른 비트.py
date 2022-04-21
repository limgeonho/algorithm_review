def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            tmp = '0' + str(bin(number)[2:])
            idx = tmp.rfind('0')
            tmp = list(tmp)
            tmp[idx] = '1'
            tmp[idx+1] = '0'
            answer.append(int(''.join(tmp), 2))
    return answer