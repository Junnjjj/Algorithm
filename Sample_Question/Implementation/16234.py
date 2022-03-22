import sys
from collections import deque

input = sys.stdin.readline

n,left,right = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]

countryUnion = [[] for _ in range(n**2)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
time = 0

def countryTerritory(i,j, visited):
  check = False    
  for v in visited:
    if not v: continue
    if v[i][j]: # True 일 경우    
      check =True      
      break
  return check

# visited = [[False] * n for _ in range(n)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(r,c):
  q = deque()
  q.append((r,c))
  visited[r][c] = True

  while q:        
    r,c = q.popleft()       
    
    for move in moves:
      dr,dc = r+move[0], c+move[1]

      if dr < 0 or dr >= n or dc < 0 or dc >= n: #범위 벗어날 경우
        continue
        
      peopleSize = map[dr][dc]      
      # 해당 영역 or 연합 인구 수의 차이가 사이일경우
      if left <= abs(map[r][c] - peopleSize) <= right and not visited[dr][dc]:
                  
        visited[dr][dc] = True
        q.append((dr,dc)) # 삽입

time = 0

unionList = []
while True:
  time += 1

  for i in range(n):
    for j in range(n):

      if time == 1: # 첫번째 경우
        if countryTerritory(i,j, unionList): # 연합에 포함되면 넘어감
          continue
          
        visited = [[False] * n for _ in range(n)]
        dfs(i,j)
  
        unionList.append(visited)
      else: # 연합을 이룬 다음
        for move in moves:
          dr,dc = i+move[0], j+move[1]
          
          if dr < 0 or dr >= n or dc < 0 or dc >= n: #범위 벗어날 경우
            continue

          if True: # dr,dc 가 i,j 와 같은 영역일 때
            
            continue

          if left <= abs(map[r][c] - peopleSize) <= right:
            
            break;

            
        # move 해서 다른 union 일 때 인구수 차이 구하고 
        pass 

  
  break

print(unionList)

for x in unionList:
  print()
  for item in x:
    print(item)

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10