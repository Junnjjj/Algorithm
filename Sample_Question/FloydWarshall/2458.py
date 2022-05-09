import sys

input = sys.stdin.readline
INF = 1e9

n,m = map(int,input().split())


graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

# a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다. 
for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1

  
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
for i in range(1,n+1):
  check = False
  for j in range(1,n+1):
    if i==j:
      continue
    if graph[i][j] == INF: # 가는 길이 없으면
      if graph[j][i] == INF: # j => i 로 가는 길이 있으면 i는 위치 확인
        check = True
        continue
  if check:
    continue
  count +=1

print(count)