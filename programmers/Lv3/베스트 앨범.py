from collections import defaultdict
def solution(genres, plays):
    answer = []
    tmp = defaultdict(list)
    genreDict = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        tmp[genre].append((idx, play))
    
    for ky in tmp.keys():
        tmp[ky].sort(key=lambda x: x[1], reverse=True)
        
    for genre, play in zip(genres, plays):
        genreDict[genre] = genreDict.get(genre, 0) + play
    
    sortedGenres = sorted(genreDict.items(), key = lambda x: x[1], reverse=True) 

    for sortedGenre in sortedGenres:
        if len(tmp[sortedGenre[0]]) == 1:
            for i in range(1):
                answer.append(tmp[sortedGenre[0]][i][0])
        else:
            for i in range(2):
                answer.append(tmp[sortedGenre[0]][i][0])

    return answer