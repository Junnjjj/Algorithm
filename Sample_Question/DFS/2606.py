
n = int(input())
m = int(input())

result = []
def dfs(graph, v, visited):
  #현재 노드를 방문처리
  visited[v] = True
  result.append(v)
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * n

#정의된 DFS 함수 호철
dfs(data, 1, visited)
print(len(result)-1)