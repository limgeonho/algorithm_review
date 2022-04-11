def solution(answers):
    answer = []
    tmp1 = [1, 2, 3, 4, 5]
    tmp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    tmp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if answers[i] == tmp1[i%len(tmp1)]:
            cnt1 += 1
        if answers[i] == tmp2[i%len(tmp2)]:
            cnt2 += 1
        if answers[i] == tmp3[i%len(tmp3)]:
            cnt3 += 1
    
    tmp = max([cnt1, cnt2, cnt3])
    
    if tmp == cnt1:
        answer.append(1)
    if tmp == cnt2:
        answer.append(2)
    if tmp == cnt3:
        answer.append(3)
    return answer