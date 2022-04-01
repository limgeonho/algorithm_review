from collections import deque

s, e = map(int, input().split())
arr = [-1] * 10001

q = deque()
q.append(s)

arr[s] = 0

while q:
    now = q.popleft()
    if now == e:
        break
    for nxt in (now+1, now-1, now+5):
        if 1<=nxt<=10000 and arr[nxt] == -1:
            arr[nxt] = arr[now] + 1
            q.append(nxt)


print(arr[e])