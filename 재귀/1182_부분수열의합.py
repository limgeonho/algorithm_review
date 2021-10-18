# 부분수열의 합
# 해당 숫자를 선택할지 하지 않을 지 (O, X) go(선택O), go(선택X)
def go(L, total):
    global answer
    if L == n:
        if total == s:
            answer += 1
        return

    go(L+1, total + array[L])
    go(L+1, total)

n, s = map(int, input().split())

array = list(map(int, input().split()))
answer = 0
go(0, 0)

if s == 0:
    answer -= 1

print(answer)