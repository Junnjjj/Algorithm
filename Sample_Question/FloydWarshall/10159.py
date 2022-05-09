import sys

input = sys.stdin.readline
INF = 1e9
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(1,n+1):
  for j in range(1,n+1):
    print(graph[i][j], end= ' ')
  print()

for i in range(1,n+1):
  count = 0
  for j in range(1,n+1):
    if i==j: continue
    if graph[i][j] == INF and graph[j][i] == INF:
      count+=1
  print(count)

# 6
# 5
# 1 2
# 2 3
# 3 4
# 5 4
# 6 5