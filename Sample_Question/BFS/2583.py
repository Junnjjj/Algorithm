import sys
sys.setrecursionlimit(10000)

m, n, k = map(int,input().split())

#m 은 x / n 은 y 좌표
graph = [[0] * n for _ in range(m)]

def bfs(x,y):
  if x < 0 or y <0 or x >=n or y >= m:
    return False , 0
  
  if graph[y][x] == 0:
    graph[y][x] = 1

    value = 1

    a = bfs(x-1,y)
    b = bfs(x+1,y)
    c = bfs(x,y-1)
    d = bfs(x,y+1)
    value += a[1] + b[1] + c[1] + d[1]
    return True, value
  return False, 0

for _ in range(k):
  x1,y1,x2,y2 = map(int,input().split())

  for y in range(y1,y2):
    for x in range(x1,x2):
      graph[y][x] = 1

result_list = []
for i in range(m):
  for j in range(n):
    result = bfs(j,i)
    if result[0] == True:
      result_list.append(result[1])

result_list.sort()
print(len(result_list))
for x in result_list:
  print(x, end=' ')
  
