import sys

input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b
    
n,m = map(int,input().split())
  
parent = [0] * (n+1) # 부모 테이블
for i in range(1,v+1):
  parent[i] = i

edges = []
for _ in range(m):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

