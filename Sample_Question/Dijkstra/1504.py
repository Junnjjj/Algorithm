import sys
import heapq

input = sys.stdin.readline

def dijkstra(start,end):
  q = []
  heapq.heappush(q,(0,start))
  distance = [1e9] * (n+1) 
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue

    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance[end]

global n
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a,b,c = map(int,input().split())
  # a,b 양방향 길이 존재, 그 거리가 
  graph[a].append((b,c))
  graph[b].append((a,c))

v1,v2 = map(int,input().split())

answer = 1e9
start = 1

for i,j in (v1,v2),(v2,v1):  
  answer = min(answer, dijkstra(start,i) + dijkstra(i,j) + dijkstra(j,n))
  
  
print(answer if answer != 1e9 else -1)

# 세준이는 1 번 정점에서 N 번 정점으로 최단 거리 이동하려고 한다
# 임의로 주어진 두 정점은 반드시 통과
# 1번에서 v1=>v2 =>n
# 1번에서 v2=>v1 =>n