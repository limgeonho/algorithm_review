def solution(absolutes, signs):
    answer = 0
    for ab, s in zip (absolutes, signs):
        if s:
            answer += ab
        else:
            answer -= ab
        
    return answer