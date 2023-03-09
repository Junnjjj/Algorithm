from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

move = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs():
  q = deque()
  q.append((0,0,k))

  visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]  
  visited[0][0][k] = 1

  while q:
    x,y,z = q.popleft()    
    if x == n-1 and y == m-1:
      return visited[x][y][z]
    
    for dx,dy in move:
      nx,ny = x+dx,y+dy      
      if 0<=nx<n and 0<=ny<m and visited[nx][ny][z] == 0:

        if graph[nx][ny] == 0:
          q.append((nx,ny,z))
          visited[nx][ny][z] = visited[x][y][z] + 1

        if z > 0 and graph[nx][ny] == 1 and visited[nx][ny][z-1] == 0:
          q.append((nx,ny,z-1))
          visited[nx][ny][z-1] = visited[x][y][z] + 1
      
  return -1

ans = bfs()
print(ans)