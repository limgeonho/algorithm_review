from itertools import permutations 

def solution(expression):
    answer = []
    changed = []
    temp = set()   
    tmp = ''

    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            changed.append(tmp)
            tmp = ''
            changed.append(e)
            temp.add(e)
    changed.append(tmp)
    
    
    for te in permutations(temp, len(temp)):
        array = changed[:]
        for t in te:
            stack = []
            while len(array) != 0:
                tmp2 = array.pop(0)
                if tmp2 == t:
                    if t == '+':
                        stack.append(str(int(stack.pop()) + int(array.pop(0))))
                    elif t == '-':
                        stack.append(str(int(stack.pop()) - int(array.pop(0))))
                    else:
                        stack.append(str(int(stack.pop()) * int(array.pop(0))))
                else:
                    stack.append(tmp2)
            array = stack
        
        answer.append(abs(int(stack[0])))
    answer.sort(reverse = True)
                
    return answer[0]