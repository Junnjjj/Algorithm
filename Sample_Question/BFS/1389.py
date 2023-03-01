from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(n,start):
  q = deque()
  result = 0
  visited = [False] * (n+1)
  q.append((start,1))
  visited[start] = True

  while q:
    prev_node,connect = q.popleft()
    
    for next_node in graph[prev_node]:
      if not visited[next_node]:
        q.append((next_node,connect+1))
        visited[next_node] = True
        result += connect

  return result

result = []
for i in range(1,n+1):
  ans = bfs(n,i)
  result.append((ans,i))

result.sort(key = lambda x:(x[0],x[1]))
print(result[0][1])