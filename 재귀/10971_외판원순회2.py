# 외판원 순회2
# 순열로 모든 경우의 수를 구한 뒤에 해당 조건에 맞게 누적시킨다 + 마지막 위치에서 처음위치로 갈 수 있는 비용추가

def go(L):
    global answer
    if L == n:
        tmp = 0
        for i in range(len(res)-1):
            if array[res[i]][res[i+1]]:
                tmp += array[res[i]][res[i+1]]
            else:
                return
        if array[res[-1]][res[0]]:
            tmp += array[res[-1]][res[0]]
        else:
            return
        if tmp < answer:
            answer = tmp
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = i
        go(L+1)
        visited[i] = False

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
res = [0] * n
answer = 987654321
go(0)
print(answer)