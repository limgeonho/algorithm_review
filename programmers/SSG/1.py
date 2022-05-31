from collections import defaultdict
from itertools import combinations

def solution(logs):
  answer = []
  scores = defaultdict(dict)
  
  for log in logs:
    id, num, score = log.split(" ")
    scores[id][num] = score
  
  tmp = []
  for key in scores.keys():
    if len(scores[key]) >=5:
      tmp.append((key, scores[key]))
  
  for comb in combinations(tmp, 2):
    if len(comb[0][1]) == len(comb[1][1]) and comb[0][1] == comb[1][1]:
      answer.append(comb[0][0]) 
      answer.append(comb[1][0]) 
    else:
      continue
    
  if not answer:
    answer = ["None"]
    return answer
  
  answer = list(set(answer))
  answer.sort()
  
  return answer




logs1 = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
logs2 = [""]
print(solution(logs))