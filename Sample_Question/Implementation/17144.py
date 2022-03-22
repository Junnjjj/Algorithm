import sys

input = sys.stdin.readline

r,c,t = map(int,input().split())
graph = []
airConditional = []
dustAir = []
for i in range(r):
  data = list(map(int,input().split()))
  graph.append(data)

  for j in range(c):
    if data[j] == -1 : # 공기 청정기 일 경우
      airConditional.append((i,j))
    elif data[j] > 0 : # 미세 먼지일 경우
      dustAir.append((i,j,data[j]))

#북 동 남 서
moves = [(-1,0), (0,1), (1,0), (0,-1)]

def dust(d_r,d_c,size):
    y,x = d_r,d_c
    count = 0
    for move in moves:
      ny,nx = y+move[0], x+move[1]
      if ny < 0 or nx < 0 or ny >= r or nx >= c or graph[ny][nx] == -1:
        count +=1
        continue
    remain = size // 5    
    for move in moves:
      ny,nx = y+move[0], x+move[1]
      if ny < 0 or nx < 0 or ny >= r or nx >= c or graph[ny][nx] == -1:      
        continue
      countMap[ny][nx] += remain
    countMap[y][x] += size - ((size//5) * (4-count))    

def conditional(d_r,d_c,type):
  if type == 1:
    dir = [1,2,3,0] #동 남 서 북
  else:
    dir = [1,0,3,2] #동 북 서 남

  dr,dc = d_r,d_c
  windIdx = 0
  temp = 0 # 새로운 바람
  
  while True:    
      
    windWay = dir[windIdx]
    nr,nc = dr + moves[windWay][0], dc + moves[windWay][1]
    if nr == d_r and nc == d_c: #제자리로 돌아온 경우
      break

    if nr <0 or nc <0 or nr >= r or nc >= c:
      windIdx += 1
      continue
    graph[nr][nc], temp = temp, graph[nr][nc] # 값 스왑
    dr,dc = nr,nc
    

time = 0
while True:
  time += 1
  
  countMap = [[0] * c for _ in range(r)]

  for d in dustAir:
    nr,nc,size = d
    dust(nr,nc,size) # 미세먼지 확산 시작

  #미세먼지 확산 후 환경
  for y in range(r):
    for x in range(c):
      if graph[y][x] != countMap[y][x] and graph[y][x] != -1:
        graph[y][x] = countMap[y][x]
  
  #공기 청정기 가동
  for i,item in enumerate(airConditional):
    conditional(item[0],item[1], i)

  if time == t:
    break

  dustAir = []
  for i in range(r):
    for j in range(c):
      if graph[i][j] > 0 : # 미세 먼지일 경우
        dustAir.append((i,j,graph[i][j]))
  
result = 0
for col in graph:  
  for item in col:
    if item > 0:
      result += item
print(result)


# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0

# [0, 0, 0, 0, 0, 0, 1, 8]
# [0, 0, 1, 0, 3, 0, 5, 6]
# [-1, 2, 1, 1, 0, 4, 6, 5]
# [-1, 5, 2, 0, 0, 2, 12, 0]
# [0, 1, 1, 0, 5, 10, 13, 8]
# [0, 1, 9, 4, 3, 5, 12, 0]
# [0, 8, 17, 8, 3, 4, 8, 4]

# [0, 0, 0, 0, 0, 1, 8, 6]
# [0, 0, 1, 0, 3, 0, 5, 5]
# [-1, 0, 2, 1, 1, 0, 4, 6]
# [-1, 0, 5, 2, 0, 0, 2, 12]
# [0, 1, 1, 0, 5, 10, 13, 0]
# [0, 1, 9, 4, 3, 5, 12, 8]
# [8, 17, 8, 3, 4, 8, 4, 0]