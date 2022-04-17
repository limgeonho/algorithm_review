def solution(n, words):
    answer = []
    
    tmp = words[0]
    temp = [words[0]]
    for i in range(1, len(words)):
        if tmp[-1] == words[i][0] and words[i] not in temp:
            tmp = words[i]
            temp.append(words[i])
        else:
            if (i+1) % n == 0:
                answer.append(n)
                answer.append((i+1) // n)
            else:
                answer.append((i+1) % n)
                answer.append((i+1) // n + 1)
            break
    else:
        answer = [0, 0]
    
    return answer