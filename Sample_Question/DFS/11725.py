import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

data = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int,input().split())
  data[a].append(b)
  data[b].append(a)

dic_result = {}

visited = [False] * (n+1)
def dfs(data, v, visited):
  
  visited[v] = True

  for x in data[v]:
    if not visited[x]:
      dic_result[x] = v #v는 x의 부모노드
      dfs(data, x, visited)
  

dfs(data,1,visited)
for i in range(2,n+1):
  print(dic_result[i])