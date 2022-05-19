n = int(input())

cnt = 0
while True:
  if n == 1:
    cnt = -1
    break
  if n == 0:
    break
  if n % 5 == 0:
    cnt += (n // 5)
    break
  else:
    n -= 2
    cnt += 1
  
  if cnt > 50000:
    cnt = -1
    break

print(cnt)