import sys

input = sys.stdin.readline
INF = 1e9
v,e = map(int,input().split())

graph =  [[INF]*(v+1) for _ in range(v+1)]


for i in range(1,v+1):
  for j in range(1,v+1):
    if i==j:
      graph[i][j] = 0

for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a][b] = c

for k in range(1,v+1):
  for i in range(1,v+1):
    for j in range(1,v+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
for i in range(1,v+1):  
  for j in range(1,v+1):
    if i==j:
      continue
    answer = min(answer, graph[i][j] + graph[j][i])

print(answer if answer != INF else -1)

# 3 4
# 1 2 1
# 3 2 1
# 1 3 5
# 2 3 2

# 4 3
# 2 3 1
# 3 4 1
# 4 2 1