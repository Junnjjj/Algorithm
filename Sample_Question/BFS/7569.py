import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())

tomato = []
for _ in range(h):
  box = [list(map(int,input().split())) for _ in range(n)]
  tomato.append(box)

# 위 아래 왼쪽 오른쪽 앞 뒤
move = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]

def find_tomato_status(tomato, h, n, m):
	ripe_tomato = []
	unripe_tomato = []	

	for i in range(h):
		for j in range(n):
			for k in range(m):
				if tomato[i][j][k] == 1:
					ripe_tomato.append((i, j, k))
				elif tomato[i][j][k] == 0:
					unripe_tomato.append((i, j, k))				

	return ripe_tomato, unripe_tomato

def bfs():
  q = deque()
  check_unripe,empty = 0,0
  sec = 0

  visited = [[[False]*m for _ in range(n)] for _ in range(h)]

  for i in range(h):
    for j in range(n):
      for k in range(m):
        if tomato[i][j][k] == 1:
          q.append((i,j,k,sec))
          visited[i][j][k] = True
        elif tomato[i][j][k] == 0:
          check_unripe += 1
        else:
          empty += 1

  if len(q) + empty == m*n*h: return 0
  
  if not q :
    # 모든 토마토가 익은 상황 
    if check_unripe > 0: return -1
    return 0

  while q:
    x,y,z,s = q.popleft()
    for dx,dy,dz in move:
      nx,ny,nz = x+dx,y+dy,z+dz
      if  0<=nx<h and 0<=ny<n and 0<=nz<m and tomato[nx][ny][nz] >= 0 and not visited[nx][ny][nz]:
        tomato[nx][ny][nz] = s+1
        q.append((nx,ny,nz,s+1))
        visited[nx][ny][nz] = True

  
  tomato_set = sum(sum(tomato,[]),[])
  if 0 in tomato_set:
    return -1
  return max(tomato_set)

def bfs2(tomato):  
  ripe_tomato, unripe_tomato = find_tomato_status(tomato,h,n,m)
  unripe_tomato_len = len(unripe_tomato)
  if unripe_tomato_len == 0:    
    return 0

  q = deque(ripe_tomato)

  sec = 0
  while True:
    # 1초가 지나면
    sec += 1
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    next_ripe_tomato = deque()
    while q:
      x,y,z = q.popleft()
      visited[x][y][z] = True

      for dx,dy,dz in move:
        nx,ny,nz = x+dx,y+dy,z+dz

        if 0<=nx<h and 0<=ny<n and 0<=nz<m and tomato[nx][ny][nz] == 0:
          next_ripe_tomato.append((nx,ny,nz))
          visited[nx][ny][nz] = True
    
    # next_ripe_tomato 는 1초가 지나면 익은 토마토의 수, 이게 0 이면 토마토 다익거나, 
    for x,y,z in next_ripe_tomato:
      tomato[x][y][z] = 1

    ripe_tomato, unripe_tomato = find_tomato_status(tomato,h,n,m)    
    # 모든 토마토가 익은 상황이면
    if len(unripe_tomato) == 0:    
      return sec
    
    # 익지 못하는 상황이면
    if unripe_tomato_len == len(unripe_tomato):      
      return -1
    
    q = deque(ripe_tomato)
    unripe_tomato_len = len(unripe_tomato)
      
    
ans = bfs()
print(ans)      

