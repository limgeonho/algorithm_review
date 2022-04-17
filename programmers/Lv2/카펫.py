def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, (total // 2)+1):
        if total % i == 0:
            a = i
            b = total // i
            if (a - 2) * (b - 2) == yellow:
                answer.append(max(a, b))
                answer.append(min(a, b))
                break
            else:
                pass
    return answer