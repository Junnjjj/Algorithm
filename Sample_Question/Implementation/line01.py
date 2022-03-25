import sys
from collections import deque
input = sys.stdin.readline

# 브라운이 코니를 잡거나
# 코니가 너무 멀리 달아나가면 게임 끝

# 코니 처음위치 C 에서 1초후 1만큼 움직이고, 이후에는 가속이 붙어 매초마다 이동거리 +1 만큼
# c, c+1, c+3, c+6  c+10...
# c, c+1, c+1 + (c+1-c+1), c+3 + (c+3)
# cn - c(n-1) + 1
# c + 3 + 1 + 
# 코니의 위치 p는  0<= p <= 200,000
# 코니가 벗어나면 게임은 끝

# 브라운은 현재위치 B에서 b-1, b+1, 2*B 만 움직일수있다
#브라운도 동일, 브라운은 벗어나는 위치로 이동 불가

c,b= map(int,input().split())
pastCony = c
conyLoaction = c

def conyMove(time):  
  global pastCony # 전전 코니 위치
  global conyLocation #전 코니 위치
  
  if time == 1:
    conyLocation = c+1
    return conyLocation

  temp = conyLocation
  conyLocation += (conyLocation - pastCony + 1)     
  pastCony = temp
 
  return conyLocation


def bfs(pony):
  global time
  q.deque()
  q.append(b)
  while q:
    brownLocation = q.popleft()
    for move in [-1,1,brwonLocation]:
      newBrownLocation = brownLocation + move
      if 0 <= newBrownLoaction <= 200000:            
        if newBrownLocation == pony:
          time = min(time, time)
          return
        else:
          q.append(newBrownLocation)

q.deque()
q.append(b)
time = 0
while True:
  time += 1

  cony = conyMove(time)
  print(cony)

  
  
  
  if cony > 200000:
    print(-1)
    break

