import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

while True:
  a,b = map(int,input().split())
  if a == -1 and b == -1:
    break
  graph[a][b] = 1
  graph[b][a] = 1

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j :
      graph[i][j] = 0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

minSum = 1e9
for i in range(1,n+1):
  minSum = min(minSum, sum(graph[i][1:]))

cand = []
score = 0
for i in range(1,n+1):
  if sum(graph[i][1:]) == minSum:
    cand.append(i)
    for j in range(1,n+1):
      score = max(score,graph[i][j])

print(score,len(cand))
for item in cand:
  print(item,end=' ')
