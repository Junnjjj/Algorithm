# # 1600 - 1
# from collections import deque
# import sys
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
# d2 = [1, 2, 2, 1, -1, -2, -2, -1]
# def bfs():
#     q = deque()
#     q.append((0, 0, k))
#     visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
#     while q:
#         x, y, z = q.popleft()
#         if x == h - 1 and y == w - 1: return visit[x][y][z]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z] == 0:
#                 visit[nx][ny][z] = visit[x][y][z] + 1
#                 q.append((nx, ny, z))
#         if z > 0:
#             for i in range(8):
#                 nx = x + d1[i]
#                 ny = y + d2[i]
#                 if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != 1 and visit[nx][ny][z - 1] == 0:
#                     visit[nx][ny][z - 1] = visit[x][y][z] + 1
#                     q.append((nx, ny, z - 1))
#     return -1
# k = int(input())
# w, h = map(int, input().split())
# s = [list(map(int, input().split())) for i in range(h)]
# print(bfs())

from collections import deque
import sys

input = sys.stdin.readline

# n,m = map(int,input().split())
# graph = [list(map(str,input().rstrip())) for _ in range(n)]

move = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

def solution():
  q = deque()
  result = 0
  visited = [[False]*m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 'o' and not visited[i][j]:
        visited[i][j] = True

        while q:
          x,y = q.popleft()
          nx,ny = x,y

          for dx,dy in move:
            # 'o' 만날때 까지 쭉 이동
            while True:
              nx,ny = nx+dx,ny+dy

              if 0<=nx<n and 0<=ny<m:
                # 다음 'o' 를 만나면
                if graph[nx][ny] == 'o' and not visited[nx][ny]:
                  q.append((nx,ny))
                  visited[nx][ny] = True
                  # 간선의 갯수 + 1
                  result += 1 
                  break
                  
              else:
                # 경계 밖으로 나가면 break
                break

  return result


# c = a+b
# d = [a+b,b+a]
# if c in d:
#   print("222")
# print(a+b)
# print(b+a)

# 4 5
# oxxxo
# oxxxx
# xxxox
# ooooo