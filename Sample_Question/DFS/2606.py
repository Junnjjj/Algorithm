
# n = int(input())
# m = int(input())

# result = []
# def dfs(graph, v, visited):
#   #현재 노드를 방문처리
#   visited[v] = True
#   result.append(v)
#   #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(graph, i, visited)

# data = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     data[a].append(b)
#     data[b].append(a)

# visited = [False] * n

# #정의된 DFS 함수 호출
# dfs(data, 1, visited)
# print(len(result)-1)

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

result = []
def dfs(graph, v, visited):
  q = deque()
  q.append(v)
  visited[v] = True
  while q:
    x = q.popleft()
    for node in graph[x]:
      if not visited[node]:
        q.append(node)
        visited[node] = True

dfs(graph,1, visited)
print(visited.count(True)-1)
    
  # visited[v] = True
  # result.append(v)
  # # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  # for i in graph[v]:
  #   if not visited[i]:
      