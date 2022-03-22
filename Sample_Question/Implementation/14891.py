import sys
from collections import deque

input = sys.stdin.readline

def roundWheel(wheel, dir):
  newWheel = deque(wheel)
  if dir == 1: # 시계 방향 회전
    temp = newWheel.pop()
    newWheel.appendleft(temp)
  elif dir == -1: # 반시계 방향 회전
    temp = newWheel.popleft()
    newWheel.append(temp)
  return newWheel

def step(idx, ordinDir):
  leftSide = wheel[idx][6]
  rightSide = wheel[idx][2]  
  cLeftSide, cRightSide = leftSide, rightSide

  wheel[idx] = roundWheel(wheel[idx], ordinDir) # 방향 회전
  dir = ordinDir
  
  leftIdx, rightIdx = idx-1,idx+1
  while leftIdx >= 0: # 왼쪽으로 무빙
    L_leftSide = wheel[leftIdx][6]
    L_rightSide = wheel[leftIdx][2]    

    if L_rightSide != leftSide: # 다른 극일 때 반대 방향으로 움직임
      dir = -1 if dir == 1 else 1
      wheel[leftIdx] = roundWheel(wheel[leftIdx], dir)
    
      leftSide = L_leftSide
      rightSide = L_rightSide
      leftIdx -= 1
    else:
      break
    

  leftSide = cLeftSide
  rightSide = cRightSide
  dir = ordinDir
  while rightIdx < 4: # 오른쪽으로 무빙     
    R_leftSide = wheel[rightIdx][6]
    R_rightSide = wheel[rightIdx][2]  
    
    if R_leftSide != rightSide: # 다른 극일 때 반대 방향으로 움직임
      dir = -1 if dir == 1 else 1
      wheel[rightIdx] = roundWheel(wheel[rightIdx], dir)
      
      leftSide = R_leftSide
      rightSide = R_rightSide
      rightIdx += 1     
    else:      
      break



wheel = [list(map(int,input().rstrip())) for _ in range(4)] #톱니봐퀴
k = int(input()) #회전의 갯수
moves = [tuple(map(int, input().split())) for _ in range(k)]

for move in moves:
  idx = move[0]-1 # 톱니 바퀴의 인덱스

  if move[1] == 1: #시계방향
    step(idx, 1)
  else: #반시계 방향
    step(idx,-1)
  
result = 0
for i,item in enumerate(wheel):
  if item[0] == 1:
    result += (2**i)
print(result)
    


# print(wheel)  

# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1

