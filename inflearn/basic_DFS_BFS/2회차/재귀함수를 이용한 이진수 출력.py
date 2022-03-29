def change(num):
    global tmp
    if num == 0:
        return tmp
    tmp += str(num % 2)
    change(num//2)

n = int(input())
tmp = ''
change(n)
print(tmp[::-1])