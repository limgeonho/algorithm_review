# 부분수열의 합
# 해당 숫자를 선택할지 하지 않을 지 (O, X) go(선택O), go(선택X)

def go(L, total):
    if L == n:
        answer[total] = True
        return
    go(L+1, total + array[L])
    go(L+1, total)


n = int(input())
array = list(map(int, input().split()))
answer = [False] * 2000000
go(0, 0)

for i in range(len(answer)):
    if not answer[i]:
        print(i)
        break
