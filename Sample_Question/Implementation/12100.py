import sys

input = sys.stdin.readline

n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]
# 0 만 빈칸
# 5번 이동시 최대 값

moves = [(0,1), (0,-1), (-1,0), (1,0)]
# 상하좌우 이동
def go(r,c,d_r,d_c,count):
  while 0 <= map[r+d_r][c+d_c] or map[r+d_r][c+d_c] < n:
    r += d_r
    c += d_r
    count +=1
  return r,c,count
  
# 좌로 이동 시 
for i in range(n):
  for j in range(n):
    if j == 0:
      temp = map[i][j]
      r,c, = i,j
      continue

    if map[i][j] == temp: # 겹칠 때 
      map[r][c] += map[i][j]
      map[i][j] = 0      
      temp = map[i][j]
    else: #다르면
      temp = map[i][j]
      c += 1
      map[r][c] = map[i][j]
    
    
  
      
# 2 0 0 2 0    
# 0 0 2 0
# 2 0 2 0    
# 2 2 0 2
# 2 4 2 0

# 3
# 2 2 2
# 4 4 4
# 8 8 8