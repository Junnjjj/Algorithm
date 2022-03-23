import sys
from collections import deque
input = sys.stdin.readline

graph = []
for i in range(12):
  data = list(input().rstrip())
  graph.append(data)

#북 동 남 서
moves = [(-1,0),(0,1),(1,0),(0,-1)]
# def gravity(): 
#   for i in range(6):
#     rowIdx = -2
#     while True:
#       if rowIdx <= -13:
#         break      
#       if graph[rowIdx][i] != '.':
#         newRowIdx = rowIdx
#         newUpRowIdx = rowIdx
#         color = graph[rowIdx][i]
#         check = False
#         while True:
#           newRowIdx += 1
#           if graph[newRowIdx][i] == '.':
#             graph[newUpRowIdx][i] = '.'
#             graph[newRowIdx][i] = color            
#             newUpRowIdx += 1
          
#           if newRowIdx == -1:
#             rowIdx -=1    
#             check = True
#             break
#         if check:
#           continue
          
                              
#       rowIdx -= 1    
def fall():
  for i in range(6):
    for j in range(10,-1,-1):
      for k in range(11,j,-1):
        if graph[j][i] != '.' and graph[k][i] == '.'

def gravity():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graph[j][i] != "." and graph[k][i] == ".":
                    graph[k][i] = graph[j][i]
                    graph[j][i] = "."
                    break

# 4개이상 연결되어 있을 경우 터짐      
def bfs(r,c):
  global count
  PyyoCount = 1
  Pyyo = [(r,c)]
  q = deque()
  q.append((r,c))
  color = graph[r][c]  
  visited[r][c] = True
  while q:
    y,x = q.popleft()
    for move in moves:
      dy = y + move[0]
      dx = x + move[1]
      if dy < 0 or dy >= 12 or dx < 0 or dx >= 6:
        continue      
      if not visited[dy][dx] and graph[dy][dx] == color:
        PyyoCount += 1
        q.append((dy,dx))
        visited[dy][dx] = True
        Pyyo.append((dy,dx))
  if PyyoCount >= 4:
    count += 1
    for dy,dx in Pyyo:
      graph[dy][dx] = '.'
          

# time = 0 # 중력 작용 하기 전 연쇄 수
# while True:
#   count = 0 # 각 각의 연쇄 수
#   visited = [[False]*6 for _ in range(12)]
  
#   for i in range(6):
#     for j in range(12):
#       if graph[j][i] != '.' and not visited[j][i]:
#         bfs(j,i)
#   gravity()

#   if count == 0:
#     if time == 0:
#       print(0)
#       break
#     print(time)
#     break
    
#   time += 1
    


gravity()
for item in graph:
  print(item)
# AAAA..
# A.....
# A.....
# A.....
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# AAAAAA

