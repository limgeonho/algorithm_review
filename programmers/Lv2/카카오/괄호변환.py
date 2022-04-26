def check(words):
    if words[0] == ')':
        return False
    stack = []
    for word in words:
        if not stack:
            stack.append(word)
        else:
            if word == '(':
                stack.append(word)
            else:
                if stack[-1] == word:
                    stack.append(word)
                else:
                    stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def change(words):
    if words == '':
        return ['', '']
    u, v = '', ''
    cnt1, cnt2 = 0, 0
    flag = True
    for i in range(len(words)):
        if flag:
            if words[i] == '(':
                cnt1 += 1
                u += words[i]
            else:
                cnt2 += 1
                u += words[i]
            if cnt1 == cnt2:
                flag = False
        else:
            v += words[i]

    return [u, v]


def calc(p):
    result = ''
    if len(p) == 0:
        return ''
    u, v = change(p)
    if check(u):
        result = u + calc(v)
    else:
        tmp = "("		
        tmp += calc(v)	
        tmp += ")"		
        u = u[1:-1]		
        for c in u:
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
        result += tmp
    return result

def solution(ps):
    if ps == '':
        answer = ''
        return
    answer = ''
    if check(ps):
        answer = ps
    else:
        answer = calc(ps)
        
    return answer