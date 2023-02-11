from collections import deque

n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


countList = []
def bfs():
  q = deque()

  for i in range(n):
    for j in range(n):
      
      count = 1      
      if graph[i][j] == 1 and not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True
        while q:
          x,y = q.popleft()
          for idx in range(4):
            nx,ny = x+dx[idx], y+dy[idx]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
              q.append((nx,ny))
              visited[nx][ny] = True
              count +=1
              
        countList.append(count)

bfs()
print(len(countList))
for x in sorted(countList):
  print(x)


# 3
# 101
# 111
# 101

