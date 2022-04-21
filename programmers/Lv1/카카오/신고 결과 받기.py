def solution(id_list, report, k):
    answer = []
    names = {}
    who = {}
    bad = []
    
    for id in id_list:
        names[id] = set()
        who[id] = []
        
    for rp in report:
        a, b = rp.split()
        names[b].add(a)
        who[a].append(b)
        
    
    for key, val in names.items():
        if len(val) >= k:
            bad.append(key)
    
    for key, val in who.items():
        cnt = 0
        for b in bad:
            if b in val:
                cnt += 1
        answer.append(cnt)
    return answer