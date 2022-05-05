# 맞는 줄 알았는데 최적이 아님... => permutations를 사용하면 시간초과!!
# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()

#     for a, b in zip(A, B):
#         if a < b:
#             answer += 1
#     return answer


def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1

    return answer