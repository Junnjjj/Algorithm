import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(input()) for _ in range(n)]

for y, row in enumerate(map):
  if 'R' in row:
    red = [y,row.index('R')]
  if 'B' in row:
    blue = [y,row.index('B')]

def go(r,c,d_r,d_c,count):
    while map[r+d_r][c+d_c]!='#' and map[r][c]!='O':
        r+=d_r
        c+=d_c
        count+=1
    return r,c,count

# 0북 1동 2남 3서
moves = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(ry,rx, by,bx, count, dir):
  q = deque()
  q.append((ry,rx,by,bx,count,dir))
  while q:
    ry,rx,by,bx,count,dir = q.popleft()       

    if count > 10:
      print('-1')
      exit()

    for i,move in enumerate(moves):
      if abs(i-dir) == 2: #위 아래 방향이므로 테스트 안해도됨
        continue
      dy,dx = move[0],move[1]
      #이동
      go_count=0
      Rr,Rc,R_count=go(ry,rx,dy,dx,go_count)
      Br,Bc,B_count=go(by,bx,dy,dx,go_count)
      
      #겹친경우
      if Rr==Br and Rc==Bc and map[Rr][Rc]!='O':
          if R_count>B_count:
              Rr-=dy
              Rc-=dx
          else:
              Br-=dy
              Bc-=dx
      
      if map[Rr][Rc] == '#' or map[Br][Bc] == '#': 
        continue
      #둘다 안빠진 경우
      if map[Rr][Rc]!='O' and map[Br][Bc]!='O':
          if (Rr,Rc,Br,Bc,count+1,i) not in q:
            q.append((Rr,Rc,Br,Bc,count+1,i))
      #레드만 빠진 경우
      elif map[Rr][Rc]=='O' and map[Br][Bc]!='O':
          if count+1 > 10:
            print(-1)
            exit()
          print(count+1)
          exit()
      else:
          continue
        
    # print(ry,rx,by,bx,q)
    # # break
        
bfs(red[0],red[1],blue[0],blue[1],0,-99)        


# 10 10 
# ##########
# #R#...##B#
# #...#.##.#
# #####.##.#
# #......#.#
# #.######.#
# #.#....#.#
# #.#.#.#..#
# #...#.O#.#
# ##########
# ##########

# 8 8
# ########
# #.####.#
# #...#B##
# #.##.R.#
# ######.#
# ##.##O.#
# ###.##.#
# ########

# 4 6
# ######
# #R####
# #B..O#
# ######

# 이게 틀림
# 4 6
# ######
# #R#O##
# #B...#
# ######