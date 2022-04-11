# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
#     completion += [''] 
#     for p in range(len(completion)):
#         if participant[p] != completion[p]:
#             answer = participant[p]
#             break
#     return answer
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]