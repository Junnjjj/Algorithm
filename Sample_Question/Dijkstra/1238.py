import sys
import heapq

INF = 1e9

input = sys.stdin.readline

n,m,x = map(int,input().split()) # N개의 마을 , M 개의 단방향 도로, X번 마을
graph = [[] for _ in range(n+1)]
for _ in range(m):
  i,j,ti = map(int,input().split())
  graph[i].append((j,ti)) # i 에서 j 까지 ti 가 걸린다.
  

def dijkstra(start, end):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist+i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance[end] # start 에서 end 까지 걸리는 최소 시간

sum_cost = [0] * (n+1)

for i in range(1,n+1):
  if i == x:
    continue
  else:
    load_cost1 = dijkstra(i,x)
    load_cost2 = dijkstra(x,i)
    sum_cost[i] = load_cost1 + load_cost2

print(max(sum_cost))

  