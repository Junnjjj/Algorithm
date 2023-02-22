from collections import deque
import sys

input = sys.stdin.readline
MAX_MAP = 100000

n,k = map(int,input().split())

visited = [-1] * (1 + MAX_MAP)

def bfs():
  q = deque()
  
  q.append(n)
  visited[n] = 0

  while q:    
    prev_n = q.popleft()
    if prev_n == k:

      return visited[prev_n]
    
    for dx in (1,-1,prev_n):
      nx = prev_n + dx
      if 0 <= nx <= MAX_MAP and visited[nx] == -1:
        if dx == prev_n:
          visited[nx] = visited[prev_n]
          q.appendleft(nx)
        else:
          visited[nx] = visited[prev_n] + 1
          q.append(nx)

ans=bfs()
print(ans)