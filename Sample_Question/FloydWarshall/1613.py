import sys
input = sys.stdin.readline
INF = int(1e9)

n,k = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0
      
for _ in range(k):
  a,b = map(int,input().split())
  graph[a][b] = 1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

s = int(input())
ans = []
for _ in range(s):
  a,b = map(int,input().split())
  if graph[a][b] != INF:
    ans.append(-1)    
  elif graph[a][b] == INF:
    if graph[b][a] != INF:
      ans.append(1)      
    else:
      ans.append(0)

for x in ans:
  print(x)


# 5 5
# 1 2
# 1 3
# 2 3
# 3 4
# 2 4
# 3
# 1 5
# 2 4
# 3 1