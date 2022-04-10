def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if not answer:
        return [-1]
    else: 
        answer.sort()
        return answer