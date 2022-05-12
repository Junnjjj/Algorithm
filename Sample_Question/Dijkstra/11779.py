import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,end):
  q = []
  heapq.heappush(q,(0,start,0))
  distance[start] = 0
  
  while q:
    dist,now,past = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost <= distance[i[0]]:
        prev = now
        past_dict[i[0]] = prev        
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0], now))
  
  idx = end
  arr = [idx]
  while True:
    prev_node = past_dict[idx]       

    if prev_node == 1: 
      arr.append(1)
      break
    arr.append(prev_node)
    idx = prev_node
    
  return distance[end], arr

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
past_dict = {v:0 for v in range(n+1)}
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

start,end = map(int,input().split())

a,past_list = dijkstra(start,end)
print(a)
print(len(past_list))
for i in range(len(past_list)-1,-1,-1):
  print(past_list[i], end=' ')