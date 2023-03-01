from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

move = [(1,0),(-1,0),(0,-1),(0,1)]

empty = []
graph = []
for i in range(n):
  row = list(map(int,input().split()))
  graph.append(row)

  for idx,j in enumerate(row):    
    if j == 0:
      empty.append((i,idx))
      
all = list(combinations(empty,3))
ans = 0

def count_zero(list):
  return sum(list,[]).count(0)

def bfs(co,zero_sum):
  q = deque()
  global ans
  count = 0
  visited = [[False]*m for _ in range(n)]

  # 2 전염 시키기
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2 and not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True

        while q:
          x,y = q.popleft()
          for dx,dy in move:
            nx,ny = x+dx,y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
              continue
            if visited[nx][ny]:
              continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2:
              continue
            if (nx == co[0][0] and ny == co[0][1]) or (nx == co[1][0] and ny == co[1][1]) or (nx == co[2][0] and ny == co[2][1]):
              continue            
            q.append((nx,ny))
            visited[nx][ny] = True
            count += 1

  remain = zero_sum - count - 3
  ans = max(ans, remain)

zero_count = count_zero(graph)
for c in all:
  bfs(c,zero_count)

print(ans)
  
  