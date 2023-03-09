import sys
from collections import deque
input = sys.stdin.readline

move = [(1,0),(-1,0),(0,1),(0,-1)]

def solution():
  q = deque()  
  visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

  # day % 2 = 1 이면 낮
  q.append((0,0,k,1))
  visited[0][0][k] = 1

  while q:
    x,y,wall,day = q.popleft()        
    if x == n-1 and y == m-1:
      return day
    
    for dx,dy in move:
      nx,ny = x+dx,y+dy
      if 0<=nx<n and 0<=ny<m and visited[nx][ny][wall] == 0:
        if graph[nx][ny] == 0:
          q.append((nx,ny,wall,day+1))
          visited[nx][ny][wall] = visited[x][y][wall] + 1
        
        if wall > 0 and graph[nx][ny] == 1 and visited[nx][ny][wall-1] == 0 and day % 2 == 1:
          q.append((nx,ny,wall-1,day+1))
          visited[nx][ny][wall-1] = visited[x][y][wall] + 1
          
        if wall > 0 and graph[nx][ny] == 1 and visited[nx][ny][wall-1] == 0 and day % 2 != 1:
          q.append((x,y,wall,day+1))
          visited[x][y][wall] = visited[x][y][wall] + 1
        
  return -1
        
    

n,m,k = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

ans = solution()
print(ans)