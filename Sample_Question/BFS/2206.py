# from collections import deque

# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#   num = list(map(int, input()))
#   num = list(map(lambda x : (x-1)*-1 , num))
#   graph.append(num)

# dx = [-1, 1, 0, 0]
# dy = [0 ,0 ,-1, 1]  

# def bfs(x,y):
#   queue = deque()
#   queue.append((x,y))
#   count = 0 # 벽 부술 수 있는 횟 수

#   while queue:
#     x,y = queue.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or ny < 0 or nx >= n or ny >= m: #공간을 벗어난 경우 무시
#         continue
#       if graph[nx][ny] == 0: #벽인 경우 무시
#         continue 
#       #부술 수 있으면 부수기
      

#       if graph[nx][ny] == 1:
#         graph[nx][ny] = graph[x][y] + 1
#         queue.append((nx,ny))

#   return graph[n-1][m-1]

# print(bfs(0,0))
# print(graph)

# # #무조건 밑 오른 쪽에서만 1일 때 (벽)일 때 한번부술수있음


M,N = 3,3
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for item in visited:
  print(item)
# print(visited)