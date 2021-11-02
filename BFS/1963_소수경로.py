# 소수 경로
# 기본적인 bfs + 소수 판별(에라토스테네스의 체)

from collections import deque

######## 에라토스테네스의 체 ########
prime = [True for _ in range(10001)]

for i in range(2, 101):
    if prime[i]:
        j = 2
        while i*j <= 10000:
            prime[i*j] = False
            j += 1
###################################

def change(num, idx, digit):
    if idx == 0 and digit == 0:
        return -1
    tmp = list(str(num))
    tmp[idx] = chr(digit + ord('0'))
    return int(''.join(tmp))

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    visited = [False] * 10001
    dist = [0] * 10001

    q = deque()
    q.append(n)
    visited[n] = True
    dist[n] = 0

    while q:
        now = q.popleft()
        if now == m:
            break
        for i in range(4):
            for j in range(10):
                nxt = change(now, i, j)
                if nxt != -1:
                    if not visited[nxt] and prime[nxt]:
                        visited[nxt] = True
                        dist[nxt] = dist[now] + 1
                        q.append(nxt)
    print(dist[m])