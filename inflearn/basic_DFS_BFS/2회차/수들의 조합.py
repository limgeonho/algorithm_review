def comb(L, start):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
        return
    for i in range(start, len(arr)):
        res[L] = arr[i]
        comb(L+1, i+1)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
res = [0] * k
cnt = 0

comb(0, 0)
print(cnt)