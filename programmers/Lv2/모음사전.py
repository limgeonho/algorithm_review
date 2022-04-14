from itertools import product
def solution(word):
    answer = 0
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        words.extend(list(product(vowels, repeat = i)))
            
    words.sort()
    tmp = tuple(word)
    answer = words.index(tmp)+1
    
    return answer