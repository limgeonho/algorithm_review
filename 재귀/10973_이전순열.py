# 이전 순열

def prev_perm(arr):
    i = len(arr) - 1
    while i > 0 and arr[i-1] <= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[i-1] <= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True

n = int(input())
array = list(map(int, input().split()))

if prev_perm(array):
    print(*array)
else:
    print(-1)