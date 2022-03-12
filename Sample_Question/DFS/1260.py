import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

linked_list = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  linked_list[a].append(b)
  linked_list[b].append(a)
  
visited_dfs = [False] * (n+1)

def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]: #방문하지 않았다면
      dfs(graph, i, visited)

move = [(0,1),(0,-1),(1,0),(-1,0)]
visited_bfs = [False] * (n+1)


def bfs(graph, v, visited):
  q = deque()
  # q.append(graph[v])
  q.append(v)
  visited[v] = True

  while q:
    x = q.popleft()
    print(x, end=' ')    
    for item in graph[x]:
      if not visited[item]: #방문하지 않았다면
        q.append(item)
        visited[item] = True



#가장작은 것부터 탐색을 위한 정렬
for x in linked_list:
  if not x: continue
  x.sort()

dfs(linked_list, v, visited_dfs)
print()
bfs(linked_list, v, visited_bfs)

