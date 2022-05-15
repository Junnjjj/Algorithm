import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(m):
  a,b = map(int,input().split()) # b가 a 보다 무겁다
  graph[b][a] = 1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    print(graph[i][j], end=' ')
  print()

answer = 0 
for i in range(1,n+1):  
  check = False
  top,down = 0,0
  for j in range(1,n+1):
    if i == j: continue

    if graph[i][j] > 0 and graph[i][j] != INF:
      top += 1

    if graph[i][j] == INF and graph[j][i] != INF and graph[j][i] > 0:
      down += 1
  
  if top > (n//2):
    answer += 1
  elif down > (n//2):
    answer += 1
    
print(answer)

# # 첫 줄에 무게가 중간이 절대로 될 수 없는 구슬의 수를 출력 한다.

# n 는 구슬의 개수, 홀수
# n // 2



# # 1 일 떄
# # 2,4,5 는 0보다 크고 3 이 INF 일 떄 이때 3에서 1로가는게 0보다 큰 경우가 아닐 경우

# # 4인 경우
# # 1,2,3 보단 크고 5 랑은 연관관계가 없을 떄

# # 0 1 x 2 1 / 2 4 5 가 무겁다
# # x 0 x 1 x
# # x x 0 1 x
# # x x x 0 x / 1 2 3 이 가볍다
# # x x x x 0