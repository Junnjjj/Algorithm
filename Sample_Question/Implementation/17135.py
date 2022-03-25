import sys

input = sys.stdin.readline

n,m,d = map(int,input().split())
graph = []
enemy = []
for i in range(n):
  data = list(map(int,input().split()))
  graph.append(data)
  for j in range(m):
    if data[j] == 1:
      enemy.append((i,j))
      
  
def searchMaxEnemy(r,c):
  global result
  ans = 0
  for e in enemy:
    enemyY = e[0]
    enemyX = e[1]
    if abs(r-enemyY) + abs(c-enemyX) <= d:
      ans += 1
  
  if ans == 0:
    return
  else:
    result = max(result, ans)
  

result = 0
for i in range(n):
  for j in range(m):
    
    searchMaxEnemy(i,j)

print(result)
    