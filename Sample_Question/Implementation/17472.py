import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 모든 섬이 이어졌나 확인하는 함수 1

# 섬에서 섬으로 다리를 만드는 함수 2

# 함수 1, 2를 전역탐색을 통해 다리의 최소값


islands = []
visited = [[False]*m for _ in range(n)]

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(r,c):
  island = []
  q = deque()
  q.append((r,c))
  visited[r][c] = True
  island.append((r,c))
  while q:
    nr,nc = q.popleft()

    for move in moves:
      dr = nr + move[0]
      dc = nc + move[1]

      if dr < 0 or dc < 0 or dr >= n or dc >= m:
        continue

      if not visited[dr][dc] and graph[dr][dc] == 1:
        q.append((dr,dc))
        island.append((dr,dc))
        visited[dr][dc] = True
        

  return island

def makeBridge(a,b):
  # a,b 는 섬 인덱스

  # a 에 가장자리에 해당하는 부분에서 가로, 세로로 뻗었을 때 b에 닿으면 연결
  # 연결된 것 중 가장 짧은 거리 리턴

  # 연결 안되면 -1 리턴 이는 해당 방식으로는 다리 이어질 수 없음
  result = 1e9
  aIsland = islands[a]
  bIsland = islands[b]
  for land in aIsland:
    ny = land[0]
    nx = land[1]

    for move in moves:
      count = 0 # 다리 길이
      dy = ny + move[0]
      dx = nx + move[1]

      if dy < 0 or dx < 0 or dy >= n or dx >= m or graph[dy][dx] == 1:
        continue
      #  바다인 경우, 해당 방향으로 1을 만날 때 까지 쭉 이동
      count += 1
      while True:
        dy = dy + move[0]
        dx = dx + move[1]

        if dy < 0 or dx < 0 or dy >= n or dx >= m: # 섬을 못만날 경우
          # count = 0
          break
        
        if graph[dy][dx] == 1: # 섬을 만나면
          # 해당 dy,dx 가 b에 해당하는지 확인
          if (dy,dx) in bIsland:
            if count != 1: # A 와 B 거리는 2 이상이여야함
              result = min(result, count)
          break
          
        count += 1

  return result if result < 1e9 else -1
  
  

#섬 추가
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      country = bfs(i,j)
      islands.append(country)

islandsCount = len(islands)
islandsIdx = list(combinations(list(map(lambda x: x, range(islandsCount))), 2))
# 연결 가능한 모든 조합 구하기
possibleBridge = list(combinations(islandsIdx, islandsCount-1))

#연결 가능한 모든 조합에서 다리가 다 연결 되지 않으면 제거
# 오류 존재 => 다 포함되어 되어 있는게 아닌 연결 시 모든 섬이 연결될 경우
newPossibleBridge = []
for i,bridge in enumerate(possibleBridge):
  # check = []
  # for item in bridge:
  #   for t in item:
  #     if not t in check:
  #       check.append(t)    

  # if len(check) != islandsCount:       
  #   continue

  q=deque()
  bVisited = [False] * islandsCount
  q.append(bridge[0][0])
  q.append(bridge[0][1])
  bVisited[bridge[0][0]] = True
  bVisited[bridge[0][1]] = True
  
  while q:
    idx = q.popleft()

    for item in bridge:
      if bVisited[item[0]] and bVisited[item[1]]: # 방문한적 있으면
        continue
      if idx == item[0] or idx == item[1]:
        q.append(item[0])
        q.append(item[1])
        bVisited[item[0]] = True
        bVisited[item[1]] = True

  check2 = False
  for ix in bVisited:
    if not ix:
      check2 = True
      break
  if check2:
    continue
  
  newPossibleBridge.append(bridge)

  
minimalBridgeSize = 1e9
for items in newPossibleBridge:
  result = 0
  check = False
  for item in items:
    Aidx = item[0]
    Bidx = item[1]

    ans = makeBridge(Aidx,Bidx)
    if ans == -1:
      check = True
      break
    result += ans    
  if check:
    continue

  if result == 8:
    print(items)
  minimalBridgeSize = min(result, minimalBridgeSize)

print(minimalBridgeSize if minimalBridgeSize < 1e9 else -1)
    

  

# 6 6
# 1 1 1 1 1 1
# 0 0 0 0 0 0
# 1 1 1 0 1 0
# 0 1 0 1 0 1
# 0 0 0 0 0 0
# 1 1 1 1 1 1

  

# 7 8
# 0 0 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 0 0
# 1 1 0 0 0 1 1 0
# 0 0 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1


# 5 6
# 1 1 0 0 0 1
# 1 1 0 0 0 1
# 0 0 0 0 0 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1


# 6 5
# 1 1 0 0 1
# 1 1 0 0 1
# 0 0 0 0 1
# 0 0 0 0 1
# 0 0 0 0 1
# 1 1 1 1 1

# 8 8
# 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1
# 1 0 0 1 1 0 0 1
# 1 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1


# 9 6
# 0 0 0 0 1 0 
# 0 0 0 0 0 0 
# 0 1 0 0 0 1 
# 0 0 0 0 0 0 
# 0 0 0 0 0 0 
# 0 1 0 0 1 1 
# 0 0 0 0 0 0 
# 0 0 0 0 0 0 
# 0 1 0 0 0 0