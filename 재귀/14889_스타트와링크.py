# 스타트와 링크
# 조합을 찾고 해당하는 가치를 누적시킨 후 최소 값 찾기

# def go(L, start):
#     global answer
#     if L == n//2:
#         tmp1 = 0
#         tmp2 = 0
#         tmp = res[:]
#         for i in range(n):
#             if i not in tmp:
#                 tmp.append(i)
#
#         for i in range((n//2)):
#             for j in range((n//2)):
#                 if i == j:
#                     continue
#                 else:
#                     tmp1 += array[tmp[i]][tmp[j]] + array[tmp[j]][tmp[i]]
#                     tmp2 += array[tmp[i+(n//2)]][tmp[j+(n//2)]] + array[tmp[j+(n//2)]][tmp[i+(n//2)]]
#
#         cost = abs(tmp1 - tmp2)
#
#         if answer > cost:
#             answer = cost
#         return
#     for i in range(start, len(array)):
#         res[L] = i
#         go(L+1, i+1)
#
# n = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
#
# res = [0] * (n//2)
# answer = 987654321
# go(0, 0)
#
# print(answer//2)

# 조합말고 O, X문제처럼 생각 -> 선택하고 선택하지 않고가 아니라 1팀이 아니라면 무조건 2팀이라고 생각
def go(L, first, second):
    global answer
    if L == n:
        if len(first) != (n//2):
            return
        if len(second) != (n//2):
            return
        tmp1 = 0
        tmp2 = 0

        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                else:
                    tmp1 += array[first[i]][first[j]]
                    tmp2 += array[second[i]][second[j]]
        cost = abs(tmp1 - tmp2)
        if cost < answer:
            answer = cost
        return

    if len(first) > (n//2):
        return
    if len(second) > (n//2):
        return
    # 추가적으로 리스트 + 리스트 = 리스트!!
    go(L+1, first + [L], second)
    go(L+1, first, second + [L])


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 987654321
go(0, [], [])

print(answer)