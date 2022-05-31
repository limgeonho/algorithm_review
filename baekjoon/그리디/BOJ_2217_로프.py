# 정렬과 밀접한 연관 + 최대, 최소 찾기
n = int(input())
rope = []
for _ in range(n):
  rope.append(int(input()))
  
rope.sort(reverse=True)

ans = []
for i in range(len(rope)):
  ans.append(rope[i] * (i+1))

print(max(ans))