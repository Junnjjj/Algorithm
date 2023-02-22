from collections import deque
import sys

input = sys.stdin.readline

move = [(1,0),(-1,0),(0,-1),(0,1)]

n,m = map(int,input().split())
graph = [list(map(str,input().rstrip())) for _ in range(n)]

ans = 0

def bfs(x,y):
  q = deque()
  global ans
  visited = [[-1]*m for _ in range(n)]

  q.append((x,y,0))
  visited[x][y] = 0
  
  while q:
    pop_x,pop_y,count = q.popleft()
    for dx,dy in move:
      nx,ny = pop_x+dx, pop_y+dy
      if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 'L' and visited[nx][ny] == -1:
        q.append((nx,ny,count+1))
        visited[nx][ny] = count + 1
        ans = max(ans, count + 1)
  
  return ans

result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      result = max(result,bfs(i,j))

print(result)