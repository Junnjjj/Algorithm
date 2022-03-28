import sys
import copy
from itertools import combinations

input = sys.stdin.readline

n,m,d = map(int,input().split())
field = []
enemy = []
for i in range(n):
  data = list(map(int,input().split()))
  field.append(data)
  
  for j in range(m):
    if data[j] == 1:
      enemy.append((i,j))
    
    
#r,c,m => r,c : 격자판, m 궁수 사정거리
def enemyMove(graph):
  move = (1,0)
  for i in range(n-1,-1,-1):
    for j in range(m):
      dy = i + move[0]
      dx = j
  
      if dy < 0 or dx < 0 or dy >= n or dx >= m:
        continue        
        
      graph[dy][dx] = graph[i][j]
      graph[i][j] = 0
  

def killEnemy(r,c,enemyList,graph):  
  count = 0
  possibleKill = ()
  for e in enemyList:
    eX,eY = e[0],e[1]
    if abs(eX-r) + abs(eY-c) <= d:      
      if not possibleKill:
        possibleKill = (eX,eY)
      elif abs(possibleKill[0]-r) + abs(possibleKill[1]-c) > abs(eX-r) + abs(eY-c) :
        possibleKill = (eX,eY)
      else:
          if possibleKill[1] > eY: #왼쪽에 있을 때, 
            possibleKill = (eX,eY)              
          else:
            continue

  if possibleKill:
    graph[possibleKill[0]][possibleKill[1]] = 0 # 적 제 거
    count += 1

  return count,possibleKill
          

def enemyCount(graph):
  count = 0
  enemyList = []
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:  
        count += 1
        enemyList.append((i,j))
  return count, enemyList

# 궁수의 위치
# m에서 3개를 뽑아서 위치리스트
# [(n,0),(n,1),(n,2)]    
archer = []
for i in range(m):
  archer.append((n,i))

archer = combinations(archer,3)

ans = 0
fieldTemp = copy.deepcopy(field)
enemyTemp = copy.deepcopy(enemy)
for Alist in archer:  
  count = 0
  while True:

    checkList = []    
    for a in Alist:      
      # 각 궁수마다 가장 가까운 적 제거      
      # count += killEnemy(a[0],a[1],enemy,field) # 제거한 적 수      
      countC, enemyIdx = killEnemy(a[0],a[1],enemy,field) # 제거한 적 수      
      count += countC
      if enemyIdx:        
        checkList.append(enemyIdx)        
      
      
      
    # 적 이동
    enemyMove(field) 
    
    # 남은 적 수, 새로운 적 리스트
    oneCount,enemy = enemyCount(field)             
        
    # 적 이 없으면 종료
    if oneCount == 0:  
      checkSize = len(checkList) - len(list(set(checkList)))      
      count = count - checkSize
      
      
      ans = max(ans,count)        
      break

  field = copy.deepcopy(fieldTemp)
  enemy = copy.deepcopy(enemyTemp)

print(ans)
    