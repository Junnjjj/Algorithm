import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]


# 짝수 짝수 일 때 방문하지 않을 한 칸 존재

if r % 2 == 0 and c % 2 == 0:
  temp,minR,minC = 1e9,0,0
  for i in range(r):
    for j in range(c):
      if i==0 and j ==0:
        continue
      if i==r-1 and j ==c-1:
        continue

      if graph[i][j] < temp:
        temp = graph[i][j]
        minR,minC = i,j


  print(minR,minC)

  
else:
  answer = []
  
  for _ in range()

  #짝수 쪽으로 출발 
  
R D L D 
# 3 3
# 5 1 3 1
# 2 4 8 2 
# 1 1 2 3