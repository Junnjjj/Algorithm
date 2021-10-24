import sys
input = sys.stdin.readline

n = int(input()) #사람 수
a,b = map(int, input().split()) #촌 수를 계산해야하는 사람
m = int(input()) #부모와 자식관계 수

linked_list = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int,input().split())
  linked_list[x].append(y)
  linked_list[y].append(x)

  #a가 b의 부모
#1의 자식 2,3   / 2의 자식 7,8,9 / 4의 자식 5,6

result = []
visited = [False] * (n+1)
count = 0
def dfs(graph, v, visited, count):
  visited[v] = True
  if v == b:
    result.append(count)
    return
    
  count += 1  

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited, count)


dfs(linked_list, a, visited, count)

if not result:
  print(-1)
else:
  print(result[0])