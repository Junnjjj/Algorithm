from collections import deque
import sys

input = sys.stdin.readline

move = [(1,0),(-1,0),(0,-1),(0,1)]

n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
population_move_count = 0

def bfs():
  global population_move_count
  q = deque()
  visited = [[False]*n for _ in range(n)]
  check = 0

  # 한번 검사
  for i in range(n):
    for j in range(n):
      union = []
      if not visited[i][j]:        
        q.append((i,j))
        visited[i][j] = True
        population = graph[i][j]
        union.append((i,j))

        while q:
          x,y = q.popleft()
          for dx,dy in move:
            nx,ny = x+dx,y+dy

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
              # 연합인지 확인
              if l<= abs(graph[x][y] - graph[nx][ny]) <= r:
                q.append((nx,ny))
                visited[nx][ny] = True
                population += graph[nx][ny]
                union.append((nx,ny))

        check += 1
        # 이동이 없을 떄
        if check == n*n:
          print(population_move_count)
          exit()
        
        new_population = population // len(union)
        for new_x,new_y in union:
          graph[new_x][new_y] = new_population

  population_move_count += 1


while True:
  bfs()
        
        

