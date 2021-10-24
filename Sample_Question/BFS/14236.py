import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
  graph = list(map(int, input().split()))
  if 9 in graph: # 아기 상어 처음 위치 
    shark_loc_x = i
    shark_loc_y = graph.index(9)
    graph[graph.index(9)] = 0 #처음 상어 위치를 0로 치환
  data.append(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
shark_size = 2
eating_count = 0
# move_count = 0

def bfs(x,y,eating_count, shark_size, move_count):

  q = deque()
  q.append((x,y,0))
  visited = [[False] * n for _ in range(n)]
  possible_eating_loc = []
  visited[x][y] = True

  while q:
    x,y,moving_count = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      #공간을 벗어난 경우 무시, 자신보다 큰 물고기를 만날겨우 무시, 방문했다면
      if nx < 0 or ny <0 or nx >= n or ny >= n or data[nx][ny] > shark_size or visited[nx][ny]:
        continue  

      #자신보다 작은 물고기 인경우, 
      if 0 < data[nx][ny] < shark_size:
        #먹은 물고기 목록을 넣고 거기서 다시 시작점으로 해서        
        possible_eating_loc.append((nx,ny,moving_count+1))

      else: #빈공간인경우 
        q.append((nx,ny,moving_count+1))
        visited[nx][ny] = True

  #물고기 선택
  possible_eating_loc.sort(key = lambda x: (x[2],x[0],x[1]))

  if not possible_eating_loc:
    #지금까지 이동 시간 return
    print(move_count)
  else:
    #정렬
    shark_loc = possible_eating_loc[0]
    # print(shark_loc)
    move_count += shark_loc[2]
    #현재 위치를 0으로
    #아기 상어 크기가 먹은 물고기랑 같아지면 크기 + 1 
    #다시 현재 위치에서 아기 상어는 먹이를 찾아서 떠남

    shark_loc_x = shark_loc[0]
    shark_loc_y = shark_loc[1]
    data[shark_loc_x][shark_loc_y] = 0

    eating_count += 1

    if shark_size == eating_count: #상어의 크기가 1 증가
      shark_size += 1
      eating_count = 0
    

    bfs(shark_loc_x,shark_loc_y, eating_count, shark_size, move_count)

bfs(shark_loc_x,shark_loc_y, eating_count, shark_size, 0)

