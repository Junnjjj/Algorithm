import sys
from collections import deque

input = sys.stdin.readline

def bfs(n,k):
  q = deque()
  k_lst= []
  visited = [1e9] * 1000000 # Cost arr
  visited[n] = 0
  q.append((n,0))

  while q:
    cur,cost = q.popleft()    
    
    if cur+1 < 1000000:            
      
    if cur-1 >= 0:
      
    if 2*cur < 1000000:
      
  
  print(visited[k])
  

N,K = map(int,input().split())

bfs(N,K)


 # 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X