import sys
import heapq 

input = sys.stdin.readline
INF = 1e9

moves = [(1,0), (0,1), (-1,0), (0,-1)]
def dijkstra(y,x):
  q = []
  distance[y][x] = 0
  heapq.heappush(q, (0,y,x))

  while q:
    dist, y,x = heapq.heappop(q)

    # if distance[now] < dist: #방문한 적 있다면
    #   continue
    if y == n-1 and x == m-1:
      continue

    for move in moves:
      ny = y + move[0]
      nx = x + move[1]
      if 0<=ny<n and 0<=nx<m:
        if distance[ny][nx] == INF:
          tmp = dist          
          if graph[ny][nx] == 1:
            tmp += 1
          distance[ny][nx] = tmp
          heapq.heappush(q, (tmp, ny,nx))
    # for i in graph[now]:
    #   cost = dist + i[0]

    #   if cost < distance[now]:
    #     distance[now] = cost

    #     heapq.heappush(q, (cost, i[1]))


# n * m 의 맵, (1,1 에서 시작), (n,m ) 으로 이동하는데 벽을 부시는 최소 갯수 구하기
n,m = map(int,input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]
dijkstra(0,0)
print(distance[n-1][m-1])



# 6 6
# 001111
# 010000
# 001111
# 110001
# 011010
# 100010