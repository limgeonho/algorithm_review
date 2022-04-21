ccccimport math
def change(x, y):
    tmp1, tmp2 = map(int, x.split(':'))
    tmp3, tmp4 = map(int, y.split(':'))
    tmp5 = 0
    if tmp2 - tmp4 >= 0:
        tmp5 += (tmp2 - tmp4)
        tmp5 += (tmp1 - tmp3) * 60
    else:
        tmp5 += (tmp2 - tmp4) + 60
        tmp5 += (tmp1-1 - tmp3) * 60
    return tmp5
    
    
    print((tmp1, tmp2))
    
def solution(fees, records):
    answer = []
    nums = {}
    calc = {}
    
    for record in records:
        time, num, status = record.split()
        nums[num] = nums.get(num, []) + [time]
    
    for key, val in nums.items():
        if len(val) % 2 != 0:
            nums[key].append('23:59')
    for key, val in nums.items():
        temp = 0
        for i in range(0, len(val), 2):
            temp += change(val[i+1], val[i])
            calc[key] = temp 
    
    final = []
    bMin, bFee, hour, fee = fees
    
    for key, val in calc.items():
        tmp = 0
        if val <= bMin:
            tmp = bFee
        else:
            tmp += bFee
            tmp += math.ceil((val-bMin) / hour) * fee
        final.append((key, tmp))
    
    final.sort()
    
    for fi in final:
        answer.append(fi[1])
    return answer
    
    