from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  u,v = map(int,input().split())

  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (n+1)

relations = [[] for _ in range(n+1)]

def bfs():
  q = deque()
  q.append(1)
  visited[1] = True

  while q:
    parent_node = q.popleft()

    for child_node in graph[parent_node]:

      if not visited[child_node]:
        q.append(child_node)
        relations[child_node].append(parent_node)
        visited[child_node] = True

bfs()
for i in range(2,n+1):
  print(relations[i][0])


    