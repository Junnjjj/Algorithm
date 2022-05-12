import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int,input().split())
items = list(map(int,input().split()))

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(r):
  a,b,c = map(int,input().split())
  graph[a][b] = c
  graph[b][a] = c

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
idx = 0
for i in range(1,n+1):
  count = 0  
  for j in range(1,n+1):
    if graph[i][j] <= m:
      count += items[j-1]

  answer = max(answer, count)
  
print(answer)

