def solution(s):
    answer = True
    
    if s[0] == ')':
        return False
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        else:
            return False
    
    if stack:
        return False
    else:
        return True