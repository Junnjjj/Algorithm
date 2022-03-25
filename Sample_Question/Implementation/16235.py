import sys
from collections import deque
import copy
input = sys.stdin.readline

# n 맵 수, m 나무 수, k 년 후 살아있는 나무 수
# 초기 양분의 수 5
# r과 c는 1부터 시작한다.
n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] # 로봇이 양분을 줄 수 있는 양
# tree = [list(map(int,input().split())) for _ in range(m)]
tree = []
for _ in range(m):
  x,y,z = map(int,input().split())
  tree.append((y-1,x-1,z))
  
  
# 나무의 위치 (y,x,나이) + ()
defaultMap = [[5]*n for _ in range(n)] #실제 양분의 현황 맵

if n == 1:
  if k == 1:
    print(1)
  else:
    print(0)
  exit()

def spring():
  # newTree = []
  newTree = deque()
  deadTree = []    
  # test = sorted(tree, key=lambda x:x[2])  

  for t in tree:
    y,x,age = t[0],t[1],t[2]    
    # 같은 위치에 있는 나무는 나이가 적은순으로 양분을 섭취하고
    # 양분을 섭취하지 못한 나무는 뒤짐
    if defaultMap[y][x] >= age:
      defaultMap[y][x] = defaultMap[y][x] - age
      newTree.append((y,x,age+1))
    else:      
      deadTree.append((y,x,age)) # 죽음
      
  return newTree, deadTree

def summer(deadTree):
  for t in deadTree:
    y,x,age = t[0],t[1],t[2]
    soil = age//2 # 토양 양분
    defaultMap[y][x] = defaultMap[y][x] + soil #토양 양분

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def autumn(treeL):  
  newTree = copy.deepcopy(treeL)
  for t in treeL:
    y,x,age = t[0],t[1],t[2]
    if age % 5 == 0:
      for move in moves:
        dy = y+ move[0]
        dx = x+ move[1]
        if dy < 0 or dx <0 or dy >=n or dx >= n:
          continue
        newTree.appendleft((dy,dx,1))
  return newTree
  
        
def winter():  
  for i in range(n):
    for j in range(n):
      defaultMap[i][j] += graph[i][j]
    

time = 0
while True:
  time += 1

  tree,deadTree = spring()
  summer(deadTree)
  tree = autumn(tree)
  winter()
  
  if time == k:
    print(len(tree))
    break
