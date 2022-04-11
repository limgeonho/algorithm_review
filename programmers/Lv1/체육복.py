def solution(n, lost, reserve):
    # 제한사항의 마지막 때문에 reserve와 lost를 재정의 하는 과정
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    answer = 0
    _reserve.sort()
    _lost.sort()
    for r in _reserve:      
        if r-1 in _lost:
            _lost.remove(r-1)
            answer += 1
            continue            
        if r+1 in _lost:
            _lost.remove(r+1)
            answer += 1
            continue           
    
    return n - len(_lost)
