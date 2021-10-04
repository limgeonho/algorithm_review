# LCS4

import sys, bisect

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

da = dict().fromkeys([i for i in range(n + 1)], -1)
db = dict().fromkeys([i for i in range(n + 1)], -1)

print(da)
print(db)
print('======================')

for i in range(n):
    da[a[i]] = i
    db[b[i]] = i

print(da)
print(db)
print('======================')


arr = []
for i in range(n):
    arr.append(db[a[i]])

print(arr)


lis = []
for i in range(n):
    if not lis:
        lis.append(arr[i])
    else:
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            idx = bisect.bisect_left(lis, arr[i])
            lis[idx] = arr[i]

print(len(lis))