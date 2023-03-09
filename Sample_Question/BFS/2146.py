import sys
from collections import deque 
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

move = [(1,0),(-1,0),(0,1),(0,-1)]


def get_length(x1,y1):
  q = deque()
  visited = [[-1] * n for _ in range(n)]
  
  q.append((x1,y1))
  color = graph[x1][y1]
  visited[x1][y1] = 0

  while q:
    x,y = q.popleft()

    for dx,dy in move:
      nx,ny = x+dx,y+dy
      
      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:

        # 가장 가까운 섬 만남
        if graph[nx][ny] != color and graph[nx][ny] > 0:
          return visited[x][y]
        
        if graph[nx][ny] == 0:
          q.append((nx,ny))
          visited[nx][ny] = visited[x][y] + 1
  
  return 1e9

def make_group(n):
  q = deque()
  visited = [[False]*n for _ in range(n)]
  island_idx = 0
  edges = []
  
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 1 and not visited[i][j]:
        island_idx += 1
        edge = []
        q.append((i,j))
        visited[i][j] = True
        graph[i][j] = island_idx

        while q:
          x,y = q.popleft()
          check = False
          for dx,dy in move:
            nx,ny = x+dx,y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
              continue
            
            if graph[nx][ny] == 0 and not check:
              edge.append((x,y))
              check = True
            
            if graph[nx][ny] == 1 and not visited[nx][ny]:
              q.append((nx,ny))
              visited[nx][ny] = True
              graph[nx][ny] = island_idx
              
        edges.append(edge)

  # 가장 자리 리스트 만들어야함 edges
  ans = 1e9 
  for edge in edges:    
    for x1,y1 in edge:
      value = get_length(x1,y1)
      ans = min(ans,value)
        
  return ans

ans = make_group(n)
print(ans)
      