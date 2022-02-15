# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# m,n = map(int, input().split())
# graph = [list(map(int,input().split())) for _ in range(m)]

# move = [(-1,0), (1,0), (0,1), (0,-1)]
# visited = [[False] * n for _ in range(m)]
# visited[0][0] = True
# result = []

# def dfs(graph, v, visited):  
#   if v[0] == m-1 and v[1] == n-1:
#     result.append(True)
#     return

#   for i in move:
#     nx = v[0] + i[0]
#     ny = v[1] + i[1]

#     if 0<= nx < m and 0<= ny <n and graph[v[0]][v[1]] > graph[nx][ny] and not visited[nx][ny]:
      
#       visited[nx][ny] = True
#       dfs(graph, (nx,ny), visited)
#       visited[nx][ny] = False

# dfs(graph, (0,0), visited)
# print(len(result))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

p = [1, 0, -1, 0]
q = [0, 1, 0, -1]
def dfs(x, y):
    if dp[x][y] != -1 : #이미 방문 했다면, 해당 dp[x][y]를 반환
        return dp[x][y]
    if (x == 0) and (y == 0): 
        return 1
    dp[x][y] = 0
    for i in range(4):
        nextX = x + p[i]
        nextY = y + q[i]
        if (0 <= nextX < m) and (0 <= nextY < n):
            if a[nextX][nextY] > a[x][y]: #값이 더 높은 곳을 찾아감
                dp[x][y] = dp[x][y] + dfs(nextX, nextY)
    return dp[x][y]
    
                
m, n=map(int,input().split())
a = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for i in range(m)]

print(dfs(m-1,n-1))