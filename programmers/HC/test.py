M, N = map(int, input().split())
A, B = map(str, input().split())

answer1 = 0
answer2 = 0

cnt = 0
idx = -1
while True:
  idx = B.find(A, idx + 1)
  if idx == -1:
    break
  cnt += 1

answer1 = cnt
answer2 = B.count(A)

final = f'{answer1} {answer2}'
print(final)