#개선된 다익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

#모든 간선 정보를 입력 받기
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

#다익스트라 알고리즘
def dijkstra(start):
  q = []
  #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q: #q 가 비어 있지 않다면
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heapop(q)
    #현재 노드가 이미 처리된적 있다면 무시
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[i]
      #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapop.heappush(q,(cost,i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
  #도달 할 수 없는 경우 무한 출력
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])