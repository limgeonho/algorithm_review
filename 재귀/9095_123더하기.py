# 1, 2, 3 더하기
# 1,2,3 중에서 한 가지를 선택(중복 순열) -> depth가 정해저 있지 않기 때문에 해당 조건으로만 탐색
# 가지치기를 했을때 O, X가 아니면 for문 사용
# 가지치기를 했을때 O, X이면 재귀 2번 -> 선택했을때 / 하지 않았을 때


def go(total):
    global answer
    if total > n:
        return
    if total == n:
        answer += 1
        return
    for i in range(1, 4):
        go(total + i)


t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0
    go(0)
    print(answer)