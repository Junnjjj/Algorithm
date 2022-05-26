import sys
input = sys.stdin.readline

INF = int(1e9)

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent,parent[x])
  return parent[x]

def union(parent,a,b):
  a = find(parent,a)
  b = find(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n,m = map(int,input().split())

parent = [0] * (n+1) # 부모 테이블
for i in range(1,n+1):
  parent[i] = i

edges = []
for _ in range(m):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

answer = 0
max_road = 0
for e in edges:
  cost,a,b = e
  if find(parent,a) != find(parent,b):
    union(parent,a,b)
    max_road = max(max_road, cost)
    answer += cost

print(answer-max_road)