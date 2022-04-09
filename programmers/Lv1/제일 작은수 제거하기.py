def solution(arr):
    answer = []
    if len(arr) <= 1:
        answer = [-1]
    else:
        tmp = min(arr)
        print(tmp)
        arr.remove(tmp)
        answer = arr
    return answer