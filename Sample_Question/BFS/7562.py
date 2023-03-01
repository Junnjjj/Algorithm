from collections import deque
import sys

input = sys.stdin.readline

move = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

def bfs(n,x1,y1,x2,y2):
  q = deque()
  q.append((x1,y1))
  visited = [[-1]*n for _ in range(n)]
  visited[x1][y1] = 0

  while q:
    x,y = q.popleft()

    for dx,dy in move:
      nx,ny = x+dx,y+dy

      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
        if nx==x2 and ny==y2:
          return visited[x][y] + 1
        
        q.append((nx,ny))
        visited[nx][ny] = visited[x][y] + 1
  

t = int(input())
result = []
for _ in range(t):
  # 체스판 한변의 길이
  l = int(input())
  x1,y1 = map(int,input().split())
  x2,y2 = map(int,input().split())
  result.append(bfs(l,x1,y1,x2,y2))

for item in result:
  if not item:
    print(0)
  else:
    print(item)
