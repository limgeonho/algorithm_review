park = [[]for _ in range(n+1)]
for floor in floors:
  if len(park[floor])+1 <= k:
    park[floor].append(1)
    answer.append(floor)
  else:
    tmp = 1
    minFloor = 0
    plusFloor = 0
    while True:
      minFloor = floor - tmp
      plusFloor = floor + tmp
      if minFloor >= 1 and len(park[minFloor]) + 1 <= k:
        park[minFloor].append(1)
        answer.append(minFloor)
        break
      if plusFloor >= 1 and len(park[plusFloor]) + 1 <= k:
        park[plusFloor].append(1)
        answer.append(plusFloor)
        break
      tmp += 1