# 차이를 최대로
# 순서를 가지고 모든 경우를 나열 => 순열

def go(L):
    global answer
    if L == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(res[i]-res[i+1])
        if answer < tmp:
            answer = tmp
        return
    for i in range(len(array)):
        if visited[i]:
            continue
        visited[i] = True
        res[L] = array[i]
        go(L+1)
        visited[i] = False

n = int(input())
array = list(map(int, input().split()))
answer = 0
res = [0] * n
visited = [False] * n
go(0)
print(answer)