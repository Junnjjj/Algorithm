import sys
import copy
from itertools import permutations

input=sys.stdin.readline

n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
rotate = [list(map(int,input().split())) for _ in range(k)]

def getArrayValue():
  result = 1e9
  for row in graph:
    result = min(result,sum(row))
  return result

# (r, c, s)로 이루어져 있고, 가장 왼쪽 윗 칸이 (r-s, c-s), 가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형을 시계 방향으로 한 칸씩 돌린다는 의미이다. 배열의 칸 (r, c)는 r행 c열을 의미한다

# 왼쪽 상단이 (r-s,c-s), 오른쪽 상단 (r-s, c+s)    r,c 는 1부터 시작
#  가운데 (r,c)
# 왼쪽 하단 (r+s,c-s) 오른쪽 하단(r+s, c+s)

  
# 동 남 서 북
moves = [(0,1),(1,0),(0,-1),(-1,0)]
def rotateArray(r,c,s):
  r,c = r-1,c-1 # 1,1 부터 시작
  for sIdx in range(1,s+1):      
  
    nr = r-sIdx
    nc = c-sIdx
    dir = 0
    while True:
      if dir == 4:        
        break
        
      dr = nr + moves[dir][0]
      dc = nc + moves[dir][1]


      if dr < r-sIdx or dc < c-sIdx or dr > r+sIdx or dc > c+sIdx:
        dir +=1        
        continue

      graph[dr][dc] = temp[nr][nc]
      nr,nc = dr,dc
      
newRotate = list(permutations(rotate,len(rotate)))
result = 1e9
GraphTemp = copy.deepcopy(graph)
for Rotate in newRotate:
  
  temp = copy.deepcopy(graph)
  for ro in Rotate:
    rotateArray(ro[0],ro[1],ro[2])  
    temp = copy.deepcopy(graph)  

  result = min(result, getArrayValue())
  graph=copy.deepcopy(GraphTemp)
print(result)