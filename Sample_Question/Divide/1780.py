# DIVIDE AND COUQUER

import sys
input = sys.stdin.readline



def solution(x,y,n):
  if same(x,y,n):       
    cnt[a[x][y]+1] += 1
    return
  m = n//3
  for i in range(3):
    for j in range(3):
      solution(x+i*m, y+j*m, m)


def same(x,y,n):
  if n == 1:
    return True
  for i in range(x,x+n):
    for j in range(y,y+n):
      if a[x][y] != a[i][j]:
        return False
  return True

N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
cnt = [0] * 3 # -1 0 1 => 0 1 2

solution(0,0,N)
for item in cnt:
  print(item)