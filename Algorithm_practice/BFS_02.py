#미로 탈출

#n, m  입력
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0 ,0 ,-1, 1]

#BFS 소스코드
def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    #현재 위체에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #공간을 벗어난 경우 무시
      if nx < 0 or ny <0 or nx >= n or ny >= m:
        continue
      #벽인 경우 무시
      if graph[nx][ny] ==0:
        continue
      #해당 노드를 처음 방문하는 경우 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))

  return graph[n-1][m-1]

<<<<<<< HEAD


=======
>>>>>>> a5d29a509f11525e80ba055761843621790cdeaa
print(bfs(0,0))
      
