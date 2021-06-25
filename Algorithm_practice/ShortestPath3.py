#플로이드 우셜 알고리즘
#모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용

INF = int(1e9)

n = int(input())
m = int(input())
#2차원 리스트를 만들고, 모든 값을 무한을 초기화

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1, n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] == 1

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c

#점화 식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("INF", end=' ')
    else:
      print(graph[a][b], end=' ')

print()