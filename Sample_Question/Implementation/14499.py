import sys
input = sys.stdin.readline

n,m,x,y,k = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [[0,0] for _ in range(3)]
#[[0,0],[0,0],[0,0]] => [위,아래], [왼쪽,오른쪽], [앞, 뒤]

moves = [(0,1), (0,-1), (-1,0), (1,0)]
# 1 동쪽, 2 서쪽, 3 북쪽, 4 남쪽
for o in order:
  dx = x + moves[o-1][0]
  dy = y + moves[o-1][1]
  if dx <0 or dx >= n or dy <0 or dy >= m:
    continue
  x,y = dx,dy  
  mapNum = data[x][y]
  
  if o == 1: # 동쪽
    dice = [[dice[1][0],dice[1][1]], [dice[0][1], dice[0][0]], [dice[2][0], dice[2][1]]]    
  elif o == 2: # 서쪽
    dice = [[dice[1][1],dice[1][0]], [dice[0][0], dice[0][1]], [dice[2][0], dice[2][1]]]
    
  elif o == 3: # 북쪽
    dice = [[dice[2][0], dice[2][1]], [dice[1][0], dice[1][1]], [dice[0][1],dice[0][0]]]
    
  else: # 남쪽
    dice = [[dice[2][1], dice[2][0]], [dice[1][0], dice[1][1]], [dice[0][0],dice[0][1]]]

  if mapNum == 0: # Map 에 써저있는 수가 0 일 경우
    data[x][y] = dice[0][1] #아랫 부분 복사            
  else: # Map 에 숫자가 써져있을 경우
    dice[0][1] = data[x][y]
    data[x][y] = 0
      
  print(dice[0][0]) #주사위 윗부분 출력