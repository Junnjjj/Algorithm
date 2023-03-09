import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

move = [(1,0),(-1,0),(0,1),(0,-1)]

def solution():
  q = deque()
  visited = [[False] * m for _ in range(n)]
  zero_group = [[0] * m for _ in range(n)]
  idx = 0

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0 and not visited[i][j]: 
        zero_list = []
        idx += 1
        sum = 1
        q.append((i,j))
        visited[i][j] = True
        zero_list.append((i,j))

        while q:
          x,y = q.popleft()
          for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and not visited[nx][ny]:
              q.append((nx,ny))
              visited[nx][ny] = True
              zero_list.append((nx,ny))
              sum += 1

        for x,y in zero_list:
          zero_group[x][y] = (sum,idx)

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        sum = 1
        idx_list = []
        for dx,dy in move:
          nx,ny = i+dx,j+dy
          if 0<=nx<n and 0<=ny<m and type(zero_group[nx][ny]) is tuple:                       
            zero_sum, zero_idx = zero_group[nx][ny]
            if zero_idx in idx_list:
              continue
            idx_list.append(zero_idx)
            sum += zero_sum            

        graph[i][j] = sum % 10
          
  for row in graph:        
    print(''.join(str(e) for e in row))
    

solution()

