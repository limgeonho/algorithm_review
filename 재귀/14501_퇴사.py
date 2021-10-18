# 퇴사
# 해당 날짜를 선택 할지 하지 않을지(O, X)선택
# -> O, X 선택 문제는 결국 전체 개수를 다 돌면서 선택여부를 따지기 때문에 L은 선택해야하는 원소들의 개수와 같음
def go(L, total):
    global answer
    if L == n:
        if total > answer:
            answer = total
        return

    if L > n:
        return

    go(L+t[L], total+p[L])
    go(L+1, total)


n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
answer = 0
go(0, 0)
print(answer)