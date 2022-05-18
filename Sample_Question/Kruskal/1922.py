import sys
input = sys.stdin.readline

# 루트 노드 찾기
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

n = int(input())
m = int(input())

parent = [v for v in range(n+1)]

edges = []
for _ in range(m):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

answer = 0
for e in edges:
  cost,a,b = e
  if find(parent,a) != find(parent,b):
    union(parent,a,b)
    answer += cost

print(answer)