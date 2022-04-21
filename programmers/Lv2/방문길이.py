def solution(dirs):
    answer = 0
    location = {'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)}
    check = set()
    sx, sy = 0, 0
    check.add((sx, sy))
    for dir in dirs:
        x, y = location[dir]
        nx = sx + x
        ny = sy + y
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            check.add((nx, ny, sx, sy))
            check.add((sx, sy, nx, ny))
            sx = nx
            sy = ny

    answer = len(check) // 2
    return answer