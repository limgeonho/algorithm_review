# 암호 만들기
# 조합... for문을 이용해서 구하고 자모음 조건을 이용해서 cut

def go(L, start):
    global res
    if L == l:
        tmp = 0
        for s in res:
            if s in vowel:
                tmp += 1
        if tmp < 1 or tmp > l-2:
            return
        print(''.join(res))
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        go(L+1, i+1)


l, c = map(int, input().split())
array = list(input().split())
array.sort()

vowel = 'aeiou'
res = [''] * l
go(0, 0)
