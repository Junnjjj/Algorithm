import sys
import copy

input = sys.stdin.readline

n,m = map(int,input().split())
#  0은 빈 칸, 6은 벽, 1~5는 CCTV
# 사각 지대의 최소 크기를 출력한다
# map = [list(map(int, input().split())) for _ in range(n)]
graph = []
cctv = []
for i in range(n):
  data = list(map(int, input().split()))  
  graph.append(data)

  for j in range(m):
    if 1 <= data[j] <= 5: # CCTV에 해당하면
      cctv.append([i,j,data[j]])

# 북 동 남 서
moves = [(-1,0), (0,1), (1,0), (0, -1)]
# CCTV mode
mode = [
  [],
  [[0],[1],[2],[3]],
  [[0,2], [1,3]],
  [[0,1],[1,2],[2,3],[0,3]],
  [[3,0,1],[0,1,2],[1,2,3],[2,3,0]],
  [[0,1,2,3]]
]

def fill(r,c, mm, board):
  for i in mm:
    nx = r
    ny = c
    while True:
      nx += moves[i][0]
      ny += moves[i][1]      

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      if board[nx][ny] == 6:
        break
      elif board[nx][ny] == 0:
        board[nx][ny] = 7

def dfs(idx, arr):
  global min_value
  
  if idx == len(cctv):
    count = 0
    for i in range(n):
        count += arr[i].count(0)
    min_value = min(min_value, count)    
    return
  temp = copy.deepcopy(arr)
  y,x,cctvNum =cctv[idx]
  for mm in mode[cctvNum]:
    fill(y,x,mm,temp)
    dfs(idx+1, temp)
    temp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0,graph)
print(min_value)
  




# 6 6
# 0 0 0 0 0 0
# 0 2 0 0 0 0
# 0 0 0 0 6 0
# 0 6 0 0 2 0
# 0 0 0 0 0 0
# 0 0 0 0 0 5

