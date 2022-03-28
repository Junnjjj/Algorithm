import sys
import heapq

input = sys.stdin.readline

r,c,m = map(int,input().split()) # r,c 격자판 크기, m 상어의 수
shark = []
for _ in range(m):
  sr,sc,s,d,z = map(int,input().split())
  shark.append((sr-1,sc-1,s,d,z))
# r, c, s, d, z  : RC 상어의 위치, s속력, d, 이동방향, z:크기

 # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을
moves = [(),(-1,0),(1,0),(0,1),(0,-1)]


def sharkMove(dr,dc,s,d,z):    
  dy,dx = dr,dc
  
  for i in range(s):
    dy = dy + moves[d][0]
    dx = dx + moves[d][1]
    
    if dy < 0 or dx < 0 or dy >= r or dx >= c:
      
      if d % 2 == 0:
        oppositeD = d-1 # 반대로 이동
      else:
        oppositeD = d+1    

      d = oppositeD

      dy = dy + (2*moves[d][0])
      dx = dx + (2*moves[d][1])
   
  return dy,dx,s,d,z


fishingMan = -1
sharkSize = []
while True:
  fishingMan += 1 # 1. 낚시왕이 오른쪽으로 한 칸 이동한다(열 idx).

  if fishingMan == c: # 낚시왕이 오른쪽 끝에 도달하면 종료 한다.
    break

  # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
  # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
  catchingShark = []
  for i,s in enumerate(shark):
    if s[1] == fishingMan:      
      heapq.heappush(catchingShark, (s[0],i,s[4]))

  if catchingShark:
    sharkRow, sharkIdx,size = heapq.heappop(catchingShark)      
    sharkSize.append(size)
    del shark[sharkIdx]

  
  # sharkMove() # 3. 상어가 이동한다. 
  newShark = []
  graph = [[False] * c for _ in range(r)]
  
  for s in shark:
    newR,newC,newS,newD,newZ = sharkMove(s[0],s[1],s[2],s[3],s[4])
    if not graph[newR][newC]:      
      graph[newR][newC] = (newR,newC,newS,newD,newZ)
    elif graph[newR][newC][4] > newZ:
      continue
    else:      
      graph[newR][newC] = (newR,newC,newS,newD,newZ)
      

  #3.2 큰상어가 작은상어를 잡아먹는다.
  for i in range(r):
    for j in range(c):
      if not graph[i][j]:
        continue      
      newShark.append(graph[i][j])

  shark = newShark
    
    
result = 0
for item in sharkSize:
  result += item
print(result)