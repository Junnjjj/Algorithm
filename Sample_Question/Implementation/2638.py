# 치즈
import sys
from collections import deque
import copy

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(arr):
  q = deque()
  q.append((0,0))
  visited[0][0] = True
  while q:
    y,x = q.popleft()
    for move in moves:
      dy = y+move[0]
      dx = x+move[1]

      if 0<=dy<n and 0<=dx<m and not visited[dy][dx]:
        if graph[dy][dx] == 0: 
          q.append((dy,dx))
          visited[dy][dx] = True
                    
        elif graph[dy][dx] == 1:
          cheeseList.append((dy,dx))
         
def findMeltingCheese(cheese):
  for c in cheese:
    count = 0
    y,x = c[0],c[1]
    for move in moves:
      dy = y + move[0]
      dx = x + move[1]
      if 0<= dy < n and 0<= dx < m:
        if visited[dy][dx]:
          count +=1
        if count >= 2:
          graph[y][x] = 0
          break
        
time = 0
while True:
  time += 1
  visited = [[False] * m for _ in range(n)]
  cheeseList = []

  temp = copy.deepcopy(graph)
  bfs(temp)
  findMeltingCheese(cheeseList)

  ans = 0
  for row in graph:
    ans += row.count(1)

  if ans == 0:
    print(time)
    break

for item in graph:
  print(item)