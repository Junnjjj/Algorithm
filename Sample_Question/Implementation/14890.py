import sys

input = sys.stdin.readline

n,l = map(int,input().split()) 
graph = [list(map(int,input().split())) for _ in range(n)]


# 북 동 남 서
moves = [(-1,0), (0, 1), (1,0), (0, -1)]
count = [[True]*n for _ in range(2)]


def go(n_r, n_c, type):
  if type == 0: # 동쪽으로
    dir = 1
    oppsiteDir = 3
  else: # 남쪽으로
    dir = 2
    oppsiteDir = 0
  
  a = type  
    
  temp = (n_r,n_c,graph[n_r][n_c])
  while True:    
    dr = temp[0] + moves[dir][0]
    dc = temp[1] + moves[dir][1]    

    # 범위를 벗어나면 종룟
    if dr < 0 or dc < 0 or dc >= n or dr >= n:
      break

    # 차이가 발생하면
    if temp[2] != graph[dr][dc]:
      if graph[dr][dc] - temp[2] == 1 : # 오르막 길
        checkR = dr + (l*moves[oppsiteDir][0])
        checkC = dc + (l*moves[oppsiteDir][1])
        checkDir = dir
        
      elif graph[dr][dc] - temp[2] == -1: #내리막 길
        checkR = temp[0] + (l*moves[dir][0])
        checkC = temp[1] + (l*moves[dir][1])
        checkDir = oppsiteDir        
        # temp = (dr,dc,graph[dc][dc])
        # 내리막 길 일 경우 위치가 좀 달라짐 처리필요
        
      else: # 높이가 2 이상일 경우      
        b = n_c if type == 0 else n_r
        count[a][b] = False
        break
        
      if checkDir == dir: # 오르막일경우
        checkT = temp[2]
      else: #내리막일경우
        checkT = graph[dr][dc]
        
      # 경사 놓을 공간이 없으면
      if checkR < 0 or checkC <0 or checkR >= n or checkC >= n or graph[checkR][checkC] != checkT:
        b = n_c if type == 0 else n_r
        count[a][b] = False
        break

      # 경사 놓을 공간이 있으면
      checkEqual = False
      for idx in range(l-1):
        checkR += moves[checkDir][0]
        checkC += moves[checkDir][1]
        if graph[checkR][checkC] != checkT:
          b = n_c if type == 0 else n_r
          count[a][b] = False
          checkEqual = True
          break
      if checkEqual:
        break
          
      if checkDir == dir: # 오르막 길 인경우
        ny,nx = dr+moves[dir][0], dc+moves[dir][1]
        if ny < 0 or nx < 0 or nx >= n or ny >= n: 
          break        
        if abs(graph[ny][nx] - graph[dr][dc]) == 1 and l == 1:
          temp = (ny,nx,graph[ny][nx])
          continue
        elif abs(graph[ny][nx] - graph[dr][dc] > 1):
          b = n_c if type == 0 else n_r
          count[a][b] = False #처리 필요
          break
        
      else: #내리막 길 인 경우
        ny,nx = temp[0]+((l+1)*moves[dir][0]), temp[1]+((l+1)*moves[dir][1])   
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          break
        if graph[ny][nx] - graph[ny+moves[oppsiteDir][0]][ny+moves[oppsiteDir][1]] == 1:
          b = n_c if type == 0 else n_r
          count[a][b] = False 
          break
        elif graph[ny][nx] - graph[ny+moves[oppsiteDir][0]][ny+moves[oppsiteDir][1]] == -1:
          ny,nx = ny+moves[oppsiteDir][0], ny+moves[oppsiteDir][1]
          temp = (ny,nx,graph[ny][nx])
          continue
          
      temp = (ny,nx,graph[ny][nx])
      
    else:
      temp = (dr,dc,graph[dr][dc])
    

      
for i,row in enumerate(graph):
  for j,col in enumerate(row):
    if i == 0:
      go(0,j, 1) # 남쪽으로
    if j == 0:
      go(i,0, 0) # 동쪽으로     

result = 0
for c in count:
  print(c)
  result += c.count(True)
print(result)

# 6 2 
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2