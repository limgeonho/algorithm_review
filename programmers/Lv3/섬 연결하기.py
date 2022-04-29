def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [0] * n
    cnt = 0
    
    for i in range(n):
        parent[i] = i
    
    costs.sort(key=lambda x:x[2])

    for cost in costs:
        a, b, co = cost 
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += co
            cnt += 1
    
    if cnt != n-1:
        print('MST 아님')
    
    return answer