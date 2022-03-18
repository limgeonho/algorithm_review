def change(n):
    global tmp
    if n == 0:
        return tmp
    else:

        tmp += str(n%2)
        change(n//2)

n = int(input())
tmp = ''
change(n)
print(int(tmp[::-1]))


def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n%2, end='')

n = int(input())
DFS(n)
