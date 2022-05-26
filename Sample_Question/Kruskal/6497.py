import sys
input = sys.stdin.readline

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent,a,b):
  a = find(parent,a)
  b = find(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


while True:
  n,m = map(int,input().split()) # 집의 수, 길의 수
  if n == 0 and m == 0:
    exit()
  
  parent = [v for v in range(n+1)]
  
  edges = []
  for i in range(m):    
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
  
  edges.sort()
  
  total = 0
  answer = 0
  for e in edges:
    cost,a,b = e
    total += cost
    if find(parent,a) != find(parent,b):
      union(parent,a,b)      
      answer += cost
  
  print(total - answer)  

  
  