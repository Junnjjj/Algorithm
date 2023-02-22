from collections import deque
import sys

input = sys.stdin.readline

move = [(1,0),(-1,0),(0,-1),(0,1)]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check_area(graph):
  q = deque()
  visited = [[False]*m for _ in range(n)]
  area = 0
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] > 0 and not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True
        area += 1

        while q:
          x,y = q.popleft()
          for nx,ny in move:
            dx,dy = x+nx,y+ny
            if 0<=dx<n and 0<=dy<m and graph[dx][dy] > 0 and not visited[dx][dy]:
              q.append((dx,dy))
              visited[dx][dy] = True

  return area

def solution():
  change_list = []
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0:
        water = 0
        
        for dx,dy in move:
          nx,ny = i+dx,j+dy
          if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            water += 1

        if water == 0:
          continue

        change_list.append((i,j,water))

  for c in change_list:
    graph[c[0]][c[1]] = graph[c[0]][c[1]] - c[2] if graph[c[0]][c[1]] - c[2] > 0 else 0

ans = 0
while True:
  if check_area(graph) == 0:
    print(0)
    exit()
  
  if check_area(graph) >= 2:
    print(ans)
    exit()
  solution()
  ans += 1


          
    
