import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
appleMap = [tuple(map(int,input().split())) for _ in range(k)]
l = int(input()) # 방향 전환 수
order = deque()
for _ in range(l):
  x,c = input().split()
  order.append((int(x),c))  

# 북0 동1 남2 서3
move = [(-1,0), (0,1),(1,0), (0,-1)]

snakeSize = 1 #뱀 길이
# snake = deque((0,0)) #뱀 형태
snake = deque() #뱀 형태
snake.append((1,1))

time = 0
x,y = 1,1 # 뱀의 처음 위치
direction = 1 #처음 방향은 동쪽으로 이동
o = order.popleft()

while True:
  if time == o[0]: # 방향 전환 타임에 도달하였을 경우
    if o[1] == 'L': #왼쪽으로 턴
      direction = 3 if direction == 0 else direction-1      
      
    else: #오른쪽으로 턴
      direction = 0 if direction == 3 else direction+1

    if len(order) != 0:
      o = order.popleft()
    else:  
      o = (0,0)
    
  time += 1 # 1초 증가
  
  ny,nx = y+move[direction][0], x+move[direction][1]  
  # 벽에 부딪치거나, 뱀 꼬리에 닿았을 때 게임 종료
  if ny == 0 or ny > n or nx ==0 or nx > n or (ny,nx) in snake:
    # print(direction, ny,nx)
    break;

  if (ny,nx) in appleMap: #애플이 있으면
    appleMap.remove((ny,nx))
    snake.append((ny,nx))
  else:
    snake.popleft()
    snake.append((ny,nx))

  y,x = ny,nx

    
print(time)
