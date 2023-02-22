from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph,V,start):
  q = deque()
  visited = [0] * (V+1)

  q.append(start)
  visited[start] = 1
    
  

t = int(input())
for _ in range(t):
  V,E = map(int,input().split())
  graph = [[] for _ in range(V+1)]
  for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)