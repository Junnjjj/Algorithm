# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n, m = map(int, input().split())

# data = [[] for _ in range(n+1)]
# for _ in range(m):
#   a,b = map(int,input().split())
#   data[b].append(a)

# result_dic = {}
# def dfs(data, v, visited):
#   visited[v] = True
#   result.append(v)

#   for x in data[v]:
#     if not visited[x]:
#       dfs(data,x,visited)

# print(data)
# for i in range(1,n+1):
#   visited = [False] * (n+1)
#   result = []
#   dfs(data,i,visited)
#   result_dic[i] = len(result)

# result = sorted(result_dic.items(), key=lambda x:x[1], reverse=True)
# a = []
# a.append(result[0][0])
# a.append(result[1][0])
# a.sort()
# print(a[0],a[1],end=' ')

from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = 1
                q.append(n)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
res = []
for i in range(1, N+1):
    check = [0]*(N+1)
    bfs(i)
    res.append(check.count(1))
m = max(res)
for i in range(N):
    if res[i] == m:
        print(i+1, end=' ')
print()