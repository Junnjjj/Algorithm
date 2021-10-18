test_count = int(input()) #TESTCASE

def bfs(x, y, n , m):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0 #방문처리
    bfs(x-1,y,n,m)
    bfs(x+1,y,n,m)
    bfs(x,y-1,n,m)
    bfs(x,y+1,n,m)
    return True
  return False

result = []
count = 0
while count < test_count:
  #가로길이 m, 세로길이 n
  m ,n ,k = map(int,input().split())
  graph = [[0] * m for _ in range(n)]

  #배추 입력
  for _ in range(k):
    x, y = map(int,input().split())
    graph[y][x] = 1 #배추벌레 위치 입력

  bug_count = 0
  for i in range(n):
    for j in range(m):
      if bfs(i,j,n,m) == True:
        bug_count += 1

  print(bug_count)
  # result.append(bug_count)

  count +=1 

# print(result)