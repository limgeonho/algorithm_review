# 해당문제는 permutations로 풀면 시간초과!!
# => sort를 사용하는 것까지 파악
# => 각각의 수를 자리수를 맞춰서 비교해야하는 것도 파악
# => 하지만 자리수를 어떤 방법으로 맞춰서 비교하지? => 몰랐음
# => 어짜피 문자열은 아스키 코드로 바뀜.. => 자리수만 *로 맞춰준다 => 끝

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x:x*3)

    return str(int(''.join(numbers)))