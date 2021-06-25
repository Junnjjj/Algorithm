#미래도시

# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF]*(n+1) for _ in range(n+1)]

# for a in range(1,n+1):
#   for b in range(1, n+1):
#     if a== b:
#       graph[a][b] == 0

# #각 간선에 대한 정보를 입력받아 그 정보를 초기화
# for _ in range(m):
#   a, b = map(int, input().split())
#   graph[a][b] = 1
#   graph[b][a] = 1

# #거쳐갈 노드 x와 k를 입력 받기
# x, k = map(int, input().split())

# for k in range(1, n+1):
#   for a in range(1, n+1):
#     for b in range(1, n+1):
#       graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# distance = graph[1][k] + graph[k][x]

# if distance >= INF:
#   print('-1')
# else:
#   print(distance)

#전보

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#간선 종류 입력받기
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y,z))


def dijkstra(start):
  q = []
  #시작 노드 설정
  heapq.headpush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.pop(q)
    if distance[now] < dist:
      continue:
    #현재 노드와 연결된 다른 노드들 확인
    for i in graph[now]:
      const = dist + i[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.headpush(q, (cost, i[0]))