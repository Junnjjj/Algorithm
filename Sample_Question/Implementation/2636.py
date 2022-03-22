import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


moves = [(1,0),(-1,0),(0,1),(0,-1)]
result = []
def bfs():
  ans = 0
  r,c = 0,0
  q = deque()
  q.append((r,c)) 
  visited[r][c] = True
  while q:
    y,x = q.popleft()
    for move in moves:
      dr = y+move[0]
      dc = x+move[1]
      
      if 0<=dr<n and 0<=dc<m and not visited[dr][dc]:
        if graph[dr][dc] == 0:
          visited[dr][dc] = True
          q.append((dr,dc))
          
        elif graph[dr][dc] == 1:
          graph[dr][dc] = 0
          visited[dr][dc] = True
          ans += 1
  result.append(ans)
  return ans

time = 0
while True:
  time += 1
  visited = [[False] * m for _ in range(n)]
  re = bfs()
  if re == 0:    
    break

print(time-1)
print(result[-2])