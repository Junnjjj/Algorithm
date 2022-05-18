import sys
import string
input = sys.stdin.readline

alpha = string.ascii_letters
alpha_dict = {k:i+1 for i,k in enumerate(alpha)}

 # a부터 z는 1부터 26을 나타내고, A부터 Z는 27부터 52
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

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
parent = [v for v in range(n+1)]

answer = 0
edges = []
for i in range(n):  
  for j in range(n):    
    cost = graph[i][j]
    if cost == '0':      
      continue 
    cost = alpha_dict[cost]
    answer += cost
    edges.append((cost,i,j))

edges.sort()

temp = []
result = 0
for e in edges:
  cost,a,b = e
  if find(parent,a) != find(parent,b):
    union(parent,a,b)
    result += cost
    temp.append(e)

if len(temp) < n-1: # 트리가 만들어지지 않으면
  print(-1)
else:
  answer -= result
  print(answer)
