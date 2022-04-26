from collections import defaultdict

def solution(tickets):
    answer = []
    airport = defaultdict(list)
    tickets.sort(reverse=True)
    
    for ticket in tickets:
        airport[ticket[0]].append(ticket[1])

    stack = ['ICN']
    while stack:
        
        tmp = stack[-1]
        
        if not airport[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(airport[tmp].pop())
            
    return answer[::-1]