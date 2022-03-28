import sys
import copy

input = sys.stdin.readline

n = int(input())
Map = [list(map(int,input().split())) for _ in range(n)]
# 0 만 빈칸
# 5번 이동시 최대 값

# 복 동 남 서
moves = [(-1,0),(0,1),(1,0),(0,-1)]
# 상하좌우 이동
def go(m,graph):
  # 0,1,2,3,4 .. n-1 로 이동
  # 북(남2)쪽 이동, 서(동1)쪽 이동 시
  if m == 2 or m == 1:
    for i in range(n):
      for j in range(n):
        y,x = i,j
        dy,dx = y,x
        while True:
          dy = dy + moves[m][0]
          dx = dx + moves[m][1]

          if dy < 0 or dx < 0 or dy >= n or dx >= n:
            break

          if graph[y][x] != 0:            
            if graph[dy][dx] == graph[y][x]:
              graph[y][x] += graph[y][x]
              graph[dy][dx] = 0
              break
            elif graph[dy][dx] > graph[y][x]:
              break
            if graph[dy][dx] == 0:
              continue
            break
          else:
            if graph[dy][dx] != 0:
              graph[y][x] = graph[dy][dx]
              graph[dy][dx] = 0
                        
  else:
    for i in range(n-1,-1,-1):
      for j in range(n-1,-1,-1):
        y,x = i,j
        dy,dx = y,x
        while True:
          dy = dy + moves[m][0]
          dx = dx + moves[m][1]

          if dy < 0 or dx < 0 or dy >= n or dx >= n:
            break

          if graph[y][x] != 0:            
            if graph[dy][dx] == graph[y][x]:
              graph[y][x] += graph[y][x]
              graph[dy][dx] = 0
              break
            elif graph[dy][dx] > graph[y][x]:              
              break
            if graph[dy][dx] == 0:
              continue
            break
            
          else:
            if graph[dy][dx] != 0:
              graph[y][x] = graph[dy][dx]
              graph[dy][dx] = 0
  return graph
        

def move(graph, count):
  global ans

  if count == 5:            
    for row in graph:      
      for item in row:
        ans = max(item,ans)      

    return
    
  temp = copy.deepcopy(graph)  
  for i in range(4):       
    move(go(i,graph), count+1)
    graph = copy.deepcopy(temp)
        
    
ans = 0
move(Map, 0)
print(ans)