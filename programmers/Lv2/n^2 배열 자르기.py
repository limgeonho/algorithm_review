def solution(n, left, right):
    answer = []

# 이거 시간초과 나버림
#     arr = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(i, n):
#             arr[i][j] = j+1
#             arr[j][i] = j+1

#     for i in range(left, right+1):
#         x = i // n
#         y = i % n
#         answer.append(arr[x][y])

#     return answer

    for i in range(left, right+1):
        x = i // n
        y = i % n
        answer.append(max(x, y) +1)
    return answer