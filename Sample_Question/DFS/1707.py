import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

q = deque()
def bfs(graph, v, visited):
  q.append(v)

  while q:
    for x in graph[q]:
      
  pass

k = int(input()) #number of test case

for _ in range(k):
  v , e = map(int, input().split())
  graph = [[] for _ in range(v+1)]
  visited = [False] * (v+1)
  for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    dfs(graph, 1, visited)
  print(graph)

#BFS를 할 때 같은 레벨의 정점끼리는 모조건 같은 색으로 칠해진다.


