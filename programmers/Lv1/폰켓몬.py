def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = list(set(nums))
    if len(nums) >= length:
        answer = length
    else:
        answer = len(nums)
    
    
    return answer