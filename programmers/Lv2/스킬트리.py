def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = list(skill)
        # 원하는 순서인지 파악하는 방법
        for s in skill_tree:
            if s in tmp:
                if s == tmp[0]:
                    tmp.pop(0)
                else:
                    break
        else:
            answer += 1
                
    return answer