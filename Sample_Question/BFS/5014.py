from collections import deque
import sys

input = sys.stdin.readline

# 1000000
F, S, G, U, D = map(int,input().split())

def solution():
  q = deque()
  visited = [-1] * (1+F)

  q.append(S)
  visited[S] = 0

  while q:
    prev_node = q.popleft()

    if prev_node == G:
      return visited[prev_node]
      
    for dx in (U, D*-1):
      nx = prev_node + dx


      if 1<= nx <= F and visited[nx] == -1:
        q.append(nx)
        visited[nx] = visited[prev_node] + 1

  return 'use the stairs'

ans = solution()
print(ans)