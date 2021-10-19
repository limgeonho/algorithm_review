# 링크와 스타트
# 선택한다 / 선택하지 않는다 => 1번팀 / 2번팀
# 조합으로 풀면 너무 복잡해짐... => 문제를 읽고 순열, 조합, 중복순열 / 부분집합인지 파악하는 것이 중요함
def go(L, first, second):
    global answer
    if L == n:
        if len(first) < 1 or len(second) < 1:
            return
        tmp1 = 0
        tmp2 = 0
        for i in range(len(first)):
            for j in range(len(first)):
                if i == j:
                    continue
                tmp1 += array[first[i]][first[j]]

        for i in range(len(second)):
            for j in range(len(second)):
                if i == j:
                    continue
                tmp2 += array[second[i]][second[j]]

        cost = abs(tmp1 - tmp2)
        if cost < answer:
            answer = cost
        return

    go(L+1, first + [L], second)
    go(L+1, first, second + [L])

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 987654321
go(0, [], [])

print(answer)