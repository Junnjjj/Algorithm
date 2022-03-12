import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r,c,d = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]

cleanMap = [[False] * m for _ in range(n)]

# 0 북, 1 동, 2 남, 3 서
move = [(-1,0), (0,1), (1,0), (0,-1)]
cleanMap[r][c] = True
count = 0
while True:  
  # 지금 방향으로 왼쪽
  nd = d - 1 if d > 0 else 3
  nx = r + move[nd][0]
  ny = c + move[nd][1]  
  if map[nx][ny] == 0 and not cleanMap[nx][ny]: #벽이 아니거나 왼쪽 구역을 방문하지 않았다면
    cleanMap[nx][ny] = True
    r,c,d = nx,ny,nd
    count = 0
    continue

  # d = nd
  # count += 1  
  if count == 4: #
  #바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    nx = r + (-1 * move[d][0])
    ny = c + (-1 * move[d][1])
    if map[nx][ny] == 1: #벽인 경우
      break    
      
    r,c = nx,ny
    count = 0
    continue  

  d = nd
  count += 1  

r = 0
for x in cleanMap:
  for i in x:
    if i: 
      r+=1
print(r)