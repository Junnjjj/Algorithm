from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def bfs(h,w,graph):
  # the number of island
  count = 0
  q = deque()
  visited = [[False]*w for _ in range(h)]

  for i in range(h):
    for j in range(w):

      if graph[i][j] == 1 and not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True
        count += 1

        while q:
          x,y = q.popleft()

          for idx in range(8):
            nx,ny = x+dx[idx], y+dy[idx]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1 and not visited[nx][ny]:
              q.append((nx,ny))
              visited[nx][ny] = True

  return count

result = []
while True:
  w,h = map(int,input().split())

  if w == 0 and h == 0:
    break

  graph = []
  for _ in range(h):
    graph.append(list(map(int,input().split())))

  ans = bfs(h,w,graph)
  result.append(ans)


print('\n'.join(list(map(lambda x:str(x), result))))
