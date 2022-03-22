import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
iceberg = []
for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(m):
    if data[j] > 0:
      iceberg.append([i,j,data[j]])
      
moves = [(-1,0), (0,1), (1,0), (0,-1)] #북 동 남 서

def dfs(y,x):
  q = deque()
  q.append((y,x))
  while q:
    r,c = q.popleft()
    visited[r][c] = True
    
    for move in moves:
      nr = r + move[0]
      nc = c + move[1]
      if nr <0 or nc < 0 or nr >= n or nc >= m or graph[nr][nc] == 0:
        continue
      if not visited[nr][nc]:
        q.append((nr,nc))
  
time = 0
while True:
  time += 1
  newIceberg = []

  for ice in iceberg:
    seaCount = 0
    r,c,iceSize = ice[0],ice[1],ice[2]
    if iceSize == 0: continue
      
    for move in moves:
      nx = ice[0] + move[0]
      ny = ice[1] + move[1]
      if nx < 0 or ny <0 or nx >= n or ny >=m:
        break
      if graph[nx][ny] == 0:
        seaCount += 1     
    iceSize = 0 if iceSize-seaCount < 0 else iceSize-seaCount
    if iceSize >= 0:
      newIceberg.append([ice[0],ice[1],iceSize])

  for ice in newIceberg:
    graph[ice[0]][ice[1]] = ice[2] #빙산을 깎아줌
  
    
  visited = [[False] * m for _ in range(n)]
  count = 0
  
  # print('iceberg',newIceberg, count)
  
  for item in newIceberg:
    if item[2] == 0: continue
    if not visited[item[0]][item[1]]:
      dfs(item[0], item[1])
      count += 1
  
  iceberg = newIceberg
  if count >= 2:
    print(time)
    break
  elif not newIceberg:
    print(0)
    break

