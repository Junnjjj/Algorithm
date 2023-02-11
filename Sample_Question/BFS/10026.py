# n = int(input())

# data = []
# data2 = []
# for _ in range(n):
#   co = input()
#   co2 = co.replace('G', 'R')
#   data.append(list(co))
#   data2.append(list(co2))
# #R G B : 일반인
# #RG B : 적녹색맹
# def bfs(x,y, color):
#   if x < 0 or y < 0 or x >= n or y >= n:
#     return False

#   if data[x][y] == color:
#     data[x][y] = 0

#     bfs(x-1,y,color)
#     bfs(x+1,y,color)
#     bfs(x,y-1,color)
#     bfs(x,y+1,color)

#     return True
#   return False

# def bfs2(x,y, color):
#   if x < 0 or y < 0 or x >= n or y >= n:
#     return False

#   if data2[x][y] == color:
#     data2[x][y] = 0

#     bfs2(x-1,y,color)
#     bfs2(x+1,y,color)
#     bfs2(x,y-1,color)
#     bfs2(x,y+1,color)

#     return True
#   return False

# count = 0
# for i in range(n):
#   for j in range(n):
#     color = data[i][j]
#     if color == 0: continue
#     if bfs(i,j,color) == True:
#       count += 1

# count2 = 0
# for i in range(n):
#   for j in range(n):
#     color = data2[i][j]
#     if color == 0: continue
#     if bfs2(i,j,color) == True:
#       count2 += 1

# print(count,count2,end=' ')

from collections import deque

# 적녹색맹 빨간생, 초록색 구분 ㄴㄴ 해
n = int(input())

graph = []
for _ in range(n):
	item = list(map(str, input()))
	graph.append(item)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(n, RB=False):
  q = deque()
  visited = [[False] * n for _ in range(n)]
  count = 0
  
  for i in range(n): 
    for j in range(n):
      
      if not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True
        count += 1
  
        while q:
          x, y = q.popleft()
          color = graph[x][y]
      
          for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
      
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
      
              if not RB:
                if graph[nx][ny] == color:
                  q.append((nx, ny))
                  visited[nx][ny] = True
              else:
                if color == 'R' or color == 'G':
                  if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif color == 'B':
                  if graph[nx][ny] == 'B':
                    q.append((nx, ny))
                    visited[nx][ny] = True
  
  return count


print(bfs(n), bfs(n, True))
