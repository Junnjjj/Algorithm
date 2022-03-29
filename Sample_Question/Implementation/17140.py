import sys

input = sys.stdin.readline

# r,c,k = map(int,input().split())
# #  A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간


# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 
# 그 다음, 수의 등장 횟수가 커지는 순으로, 
# 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 
# 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.


# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. 
# R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 
# 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 
# 수를 정렬할 때 0은 무시해야 한다.  예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.

# [3,1,1] => [3,1,1,2] => [2, 1, 3, 1, 1, 2]
# 3이 한번, 1이 두번

# 3이 한번, 1이 두번, 2가 한번

# 2, 1, 3, 1, 2 ,1 

def sorting(numList):  
  numCount = [0] * (max(numList) + 1)
  for num in numList:
    numCount[num] += 1

  numTupleList = []
  for i,n in enumerate(numCount):
    if i == 0: # 정렬할 때 0 은 무시
      continue
    if n != 0:
      numTupleList.append((i,n))

  numTupleList = sorted(numTupleList, key=lambda x: (x[1],x[0]))
  newLine = []
  for item in numTupleList:
    newLine.append(item[0])
    newLine.append(item[1])
  return newLine


# a = [1,2,1]
  
# print(sorting(a))

graph = [[0]*101 for _ in range(101)]
r,c,k = map(int,input().split())
for i in range(3):
  a,b,cc = map(int,input().split())

  graph[i+1][1] = a
  graph[i+1][2] = b
  graph[i+1][3] = cc


time = 0
rSize,rSizeTemp = 3,3
cSize,cSizeTemp = 3,3
while True:
  if graph[r][c] == k:
    print(time)
    break
  elif time == 101 and graph[r][c] != k:
    print(-1)
    break
  
  time += 1

  if rSize >= cSize: # R연산
    for i in range(rSize):
      # i+1 
      newRow = sorting(graph[i+1]) #list      
      cSizeTemp = max(cSizeTemp, len(newRow))

      for j in range(1,101):
        if j >len(newRow):
          graph[i+1][j] = 0
          continue        
        graph[i+1][j] = newRow[j-1]
        
    cSize = cSizeTemp
        
  else: # C연산
    for i in range(1,cSize+1):
      colList = []
      colIdx = i
      for j in range(1,rSize+1):
        colList.append(graph[j][i])

      newCol = sorting(colList)      
      rSizeTemp = max(rSizeTemp, len(newCol))

      for ko in range(1,101):
        if ko > len(newCol):
          graph[ko][i] = 0
          continue
        graph[ko][i] = newCol[ko-1]

    rSize = rSizeTemp  

  

# for item in graph:
#   print(item)
# for i in range(4):
#   print(graph[1][i])