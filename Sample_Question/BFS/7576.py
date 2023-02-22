import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

move = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs():
  q = deque()
  check_unripe,empty = 0,0
  sec = 0

  visited = [[False]*m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if tomato[i][j] == 1:
        q.append((i,j,sec))
        visited[i][j] = True
      elif tomato[i][j] == 0:
        check_unripe += 1
      else:
        empty += 1

  if len(q) + empty == m*n:
    return 0
  
  if not q :
    # 모든 토마토가 익은 상황 
    if check_unripe > 0: return -1
    return 0
    
  while q:
    x,y,s = q.popleft()
    for dx,dy in move:
      nx,ny = x+dx,y+dy
      if 0<=nx<n and 0<=ny<m and tomato[nx][ny] >= 0 and not visited[nx][ny]:
        tomato[nx][ny] = s+1
        q.append((nx,ny,s+1))
        visited[nx][ny] = True

  
  tomato_set = sum(tomato,[])
  if 0 in tomato_set:
    return -1
  return max(tomato_set)
      
ans = bfs()
print(ans)

# print(tomato)

# 2 2
# -1 0
# 0 -1

# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1