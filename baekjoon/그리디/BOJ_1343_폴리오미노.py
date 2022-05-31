def check(ans, cn):
  while True:
    if cn == 0:
      break
    if cn == 1:
      ans = -1
      break
    if cn >= 4:
      ans += 'AAAA'
      cn -= 4
    else:
      ans += 'BB'
      cn -= 2
  return ans
poly = input()
cnt = 0


answer = ''
for po in poly:
  if po == 'X':
    cnt += 1
  else:
    tmp = check(answer, cnt)
    if tmp == -1:
      break
    answer = tmp
    answer += '.'
    cnt = 0

if cnt != 0:
  tmp = check(answer, cnt)
  answer = tmp

print(answer)
