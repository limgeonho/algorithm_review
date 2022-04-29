def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = routes[0][1]
    answer = 1
    
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            answer += 1
            camera = routes[i][1]
        else:
            continue
            
    return answer