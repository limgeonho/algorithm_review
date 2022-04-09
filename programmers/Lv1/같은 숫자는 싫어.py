def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if tmp == arr[i]:
            pass
        else:
            answer.append(arr[i])
            tmp = arr[i]
    return answer