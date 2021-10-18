n = int(input())

data = []
data2 = []
for _ in range(n):
  co = input()
  co2 = co.replace('G', 'R')
  data.append(list(co))
  data2.append(list(co2))
#R G B : 일반인
#RG B : 적녹색맹
def bfs(x,y, color):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False

  if data[x][y] == color:
    data[x][y] = 0

    bfs(x-1,y,color)
    bfs(x+1,y,color)
    bfs(x,y-1,color)
    bfs(x,y+1,color)

    return True
  return False

def bfs2(x,y, color):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False

  if data2[x][y] == color:
    data2[x][y] = 0

    bfs2(x-1,y,color)
    bfs2(x+1,y,color)
    bfs2(x,y-1,color)
    bfs2(x,y+1,color)

    return True
  return False  

count = 0
for i in range(n):
  for j in range(n):
    color = data[i][j]
    if color == 0: continue
    if bfs(i,j,color) == True:
      count += 1

count2 = 0
for i in range(n):
  for j in range(n):
    color = data2[i][j]
    if color == 0: continue
    if bfs2(i,j,color) == True:
      count2 += 1

print(count,count2,end=' ')
