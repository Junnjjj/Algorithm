import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[]]

for _ in range(n):
  row = [INF]+list(map(int,input().split()))    
  graph.append(row)

check = [[False] * (n+1) for _ in range(n+1)]

for k in range(1,n+1):
  for i in range(1,n+1):
    if k == i: continue
    for j in range(1,n+1):
      if k == j or i == j: continue      
        
      if graph[i][j] > graph[i][k] + graph[k][j]:        
        print(-1)
        exit()
      
      if graph[i][j] == graph[i][k] + graph[k][j]:
        check[i][j] = True

answer = 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if not check[i][j]:
      answer += graph[i][j]

print(int(answer/2))
