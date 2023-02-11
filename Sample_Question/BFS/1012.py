# test_count = int(input()) #TESTCASE

# def bfs(x, y, n , m):
#   if x < 0 or x >= n or y < 0 or y >= m:
#     return False

#   if graph[x][y] == 1:
#     graph[x][y] = 0 #방문처리
#     bfs(x-1,y,n,m)
#     bfs(x+1,y,n,m)
#     bfs(x,y-1,n,m)
#     bfs(x,y+1,n,m)
#     return True
#   return False

# result = []
# count = 0
# while count < test_count:
#   #가로길이 m, 세로길이 n
#   m ,n ,k = map(int,input().split())
#   graph = [[0] * m for _ in range(n)]

#   #배추 입력
#   for _ in range(k):
#     x, y = map(int,input().split())
#     graph[y][x] = 1 #배추벌레 위치 입력

#   bug_count = 0
#   for i in range(n):
#     for j in range(m):
#       if bfs(i,j,n,m) == True:
#         bug_count += 1

#   print(bug_count)
#   # result.append(bug_count)

#   count +=1 

# # print(result)

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, n, m):
  q = deque()
  visited = [[False] * m for _ in range(n)]
  count = 0
  
  for i in range(n):
    for j in range(m):

      if graph[i][j] == 1 and not visited[i][j]:
        q.append((i,j))
        visited[i][j] = True

        while q:
          di,dj = q.popleft()
          for idx in range(4):
            ni,nj = di+dx[idx], dj+dy[idx]

            if 0<=ni<n and 0 <= nj <m and graph[ni][nj] == 1 and not visited[ni][nj]:
              q.append((ni,nj))
              visited[ni][nj] = True
       
        count += 1

  return count
  

# lenght of test Case 
t = int(input()) 
result = []
for _ in range(t):
  # 가로길이 M, 세로길이 n, 배추 갯수 k
  m,n,k = map(int,input().split())

  graph = [[0] * m for _ in range(n)]
  
  for _ in range(k):
    a,b = map(int,input().split())
    graph[b][a] = 1

  ans = bfs(graph, n, m)
  result.append(ans)  

for x in result:
  print(x)

  

