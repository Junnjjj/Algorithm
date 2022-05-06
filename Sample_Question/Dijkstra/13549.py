# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n,k = map(int,input().split())

q = deque()
q.append(n)
visited = [-1] * (100001)
visited[n] = 0

while q:
  s = q.popleft()    
  if s == k:
    print(visited[s])
    break
  if 0 <= s-1 < 100001 and visited[s-1] == -1:
    visited[s-1] = visited[s] + 1
    q.append(s-1)
  if 0 <= 2*s < 100001 and visited[2*s] == -1:
    visited[2*s] = visited[s]
    q.appendleft(2*s)
  if 0 < s+1 < 100001 and visited[s+1] == -1:
    visited[s+1] = visited[s] + 1
    q.append(s+1)    
    
  

