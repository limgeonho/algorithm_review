from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    weight = deque(people)

    while weight:

        if len(weight) == 1:
            weight.pop()
            answer += 1
        else:
            if weight[0] + weight[-1] <= limit:
                answer += 1
                weight.pop()
                weight.popleft()
            else:
                weight.popleft()
                answer += 1
    return answer