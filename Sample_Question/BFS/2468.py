import sys
sys.setrecursionlimit(10000)

n = int(input())

data = []
water = []
for _ in range(n):
  data.append(list(map(int,input().split())))

water = list(set(sum(data, [])))

def bfs(x,y, visited, water_size):
  if x < 0 or y <0 or x >= n or y >= n or visited[x][y] == True:
    return False

  if data[x][y] > water_size:
    visited[x][y] = True #방문처리

    bfs(x-1,y, visited, water_size)
    bfs(x+1,y, visited, water_size)
    bfs(x,y-1, visited, water_size)
    bfs(x,y+1, visited, water_size)
    return True
  return False
  
result = 0
for water_size in water:
  visited = [[False] * n for _ in range(n)]  #방문확인을 위한 list

  land = 0
  for i in range(n):
    for j in range(n):
      if bfs(i, j, visited, water_size) == True:
        land += 1

  if land > result:
    result = land

if result == 0:
  print(1)
else:
  print(result)       
  
