# 해당 풀이는 정확성 검사는 통과하지만 효율성 통과는 실패...
# 해당 문제의 효율성을 통과하기 위해서는 딕셔너리 + 이분탐색(정렬된 상태에서 빠르게 원하는 값을 찾아낼 때 사용)

def solution(info, query):
    answer = []
    participants = []
    conditions = []
    
    for inf in info:
        lang, befe, js, food, score = inf.split()
        participants.append((lang, befe, js, food, score))
    
    participants.sort(key=lambda x:(x[0], x[1], x[2], x[3], x[4]))
    
    for q in query:
        lang, befe, js, foodScore = list(q.split(' and '))
        food, score = foodScore.split()
        if lang == '-':
            lang = ['cpp', 'java', 'python']
        if befe == '-':
            befe = ['backend', 'frontend']
        if js == '-':
            js = ['junior', 'senior']
        if food == '-':
            food = ['chicken', 'pizza']
        conditions.append((lang, befe, js, food, int(score)))

    
    for condition in conditions:
        lang1, befe1, js1, food1, score1 = condition
        cnt = 0
        for part in participants:
            lang2, befe2, js2, food2, score2 = part
            if lang2 in lang1 and befe2 in befe1 and js2 in js1 and food2 in food1 and int(score2) >= int(score1):
                cnt += 1
        answer.append(cnt)
    
    return answer

##########################################################################################
# 모든 나올 수 있는 경우를 딕셔너리로 저장한다.

from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        key = info[:-1]
        val = int(info[-1])
        
        for i in range(5):
            for comb in combinations(key, i):
                tmp_key = ''.join(comb)
                info_dict[tmp_key].append(val)
                
    for key in info_dict.keys():
        info_dict[key].sort()
        
    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]
        
        
        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)
        
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while start < end:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer