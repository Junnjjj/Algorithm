import sys
sys.setrecursionlimit(10**6)

n = int(input())

data = []
for _ in range(n):
  data.append(list(map(int, input())))

def bfs(x,y):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False, 0

  if data[x][y] == 1:
    data[x][y] = 0

    value = 1
    a = bfs(x-1,y)
    b = bfs(x+1,y)
    c = bfs(x,y-1)
    d = bfs(x,y+1)
    value += a[1] + b[1] + c[1] + d[1]  
    return True, value
  return False, 0

result_list = []
for i in range(n):
  for j in range(n):
    result = bfs(i,j)
    if result[0] == True:
      result_list.append(result[1])

print(len(result_list))
result_list.sort()
for x in result_list:
  print(x)


