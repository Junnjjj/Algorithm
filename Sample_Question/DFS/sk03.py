from collections import deque
import sys
import copy

input = sys.stdin.readline

move = [(1,0),(-1,0),(0,1),(0,-1)]

n,m = map(int,input().split())
graph = []
count_one = 0
for i in range(n):
  row = list(map(int,input().split()))
  graph.append(row)
  count_one += row.count(1)
  if 2 in row:
    start = (i,row.index(2))  

visited = [[False]*m for _ in range(n)]
# 첫 스타트 위치 방문 처리
visited[start[0]][start[1]] = True

def check_all_visit(visited):
  one_dimension_visit = sum(visited,[]) 

  count_of_visited = one_dimension_visit.count(True)

  return True if count_of_visited == (n*m)-count_one else False
  

def solution(start, visited):

  x,y = start[0],start[1]
  # # 디버깅
  # print(x,y)
  # for row in visited:
  #   print(row)
  
  result = check_all_visit(visited)
  if result:
    print(1)
    exit()
    
  copy_visited = copy.deepcopy(visited)
  
  start_x,start_y = x,y
  
  for nx,ny in move:
    # 한쪽 방향으로 경계나, 1, 방문한 칸 만날 때 까지 이동
    while True:
      dx,dy = x+nx,y+ny
      
      if 0<=dx<n and 0<=dy<m and graph[dx][dy] == 0 and not copy_visited[dx][dy]:
        copy_visited[dx][dy] = True

        x,y = dx,dy

      else:
        x,y = start_x,start_y        
        break

    
    new_start = (dx-nx,dy-ny)
    if new_start[0] == start_x and new_start[1] == start_y:
      continue
    solution(new_start,copy_visited)

    copy_visited = visited
  
solution(start,visited)
print(0)

# 4 5
# 1 1 1 0 0
# 2 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 1

# 3 3
# 1 1 2
# 0 0 0
# 1 1 1

# 3 3
# 1 0 1
# 0 2 0
# 1 0 1

# 3 5
# 1 2 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1

# 3 5
# 1 2 1 1 1
# 1 0 0 0 0
# 1 0 0 0 1