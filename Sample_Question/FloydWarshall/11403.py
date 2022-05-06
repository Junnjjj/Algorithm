# import sys

# input = sys.stdin.readline

# INF = int(1e9)

# n = int(input())

# graph = [[]]+[[INF]+list(map(int,input().split())) for _ in range(n)]

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if graph[i][j] == 0:
#       graph[i][j] = INF

# for k in range(1,n+1):
#   for a in range(1,n+1):
#     for b in range(1,n+1):
#       graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if graph[i][j] != INF and graph[i][j] != 0:
#       print(1, end=' ')
#     else:
#       print(0, end=' ')
#   print()

a = 100
result = 0
for i in range(1,3):
   result = a >> i
   print(result)
   result = result + 1
   print(result)
pirnt(result)