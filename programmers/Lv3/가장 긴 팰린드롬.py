def check(s):
    if s == s[::-1]:
        return True
    else:
        return False

def solution(s):
    answer = 1
        
    for i in range(len(s)):
        tmp = s[i]
        for j in range(i+1, len(s)):
            tmp += s[j]
            if check(tmp):
                if len(tmp) > answer:
                    answer = len(tmp)
    
    return answer