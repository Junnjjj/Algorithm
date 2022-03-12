import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

chickenShop = []
home = []
for x in range(n):
  for y in range(n):
    if map[x][y] == 2:
      chickenShop.append((x,y))
    elif map[x][y] == 1:
      home.append((x,y))

# m 만큼 치킨집 조합의 갯수 구하기 

result = 1e+9
remainChickenShop = list(combinations(chickenShop, m))
for shop in remainChickenShop:
  sum = 0
  for homeXY in home:
    distance = 2*n
    for shopXY in shop:
      dx = shopXY[0] - homeXY[0]
      dy = shopXY[1] - homeXY[1]
      if(distance > abs(dx) + abs(dy)):
        distance = abs(dx) + abs(dy)
  
      if distance == 1: #거리가 1 일 때 나머지 안찾아도됨
        continue

    sum += distance  #거리의 치킨 거리 

  result = min(result, sum)

print(result)
  
  

