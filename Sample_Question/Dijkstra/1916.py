import sys
import heapq

input = sys.stdin.readline
INF = 1e9

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수 (간선의 개수)
graph = [[] for _ in range(n+1)]


# a 출발 도시, b 도착 도시, c 비용
info = []
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c)) # a 에서 b 로 가는 비용 c

start,end = map(int,input().split()) # 출발도시, 도착도시

distance = [INF] * (n+1)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    # 현재 노드가 이미 처리된 노드라면 무시
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(distance[end])
# start 에서 end 로 가는 최소 비용 구하기




# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5