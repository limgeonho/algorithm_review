# 로또
# 조합 문제 => array 중에서 하나씩 뽑아서 선택(for문)

def go(L, start):
    if L == 6:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        go(L+1, i+1)

while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break

    number = lotto[0]
    array = lotto[1:]
    visited = [False] * len(array)
    res = [0] * 6

    go(0, 0)
    print()


