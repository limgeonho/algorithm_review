from collections import deque

def check(ss):
    stack = []
    if ss[0] == ')' or ss[0] == '}' or ss[0] == ']':
        return False
    for s in ss:
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        else:
            if not stack:
                return False
            elif s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
    
    if len(stack):
        return False
    else:
        return True
            
        
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        # tmp = s.popleft()
        # s.append(tmp)
        s.rotate(-1)
        if check(s):
            answer += 1
    return answer