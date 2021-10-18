# 1, 2, 3 더하기

def go(s, goal):
    global answer
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s+i, goal)
    return now

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0

    print(go(0, n))