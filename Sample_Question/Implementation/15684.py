import sys

input = sys.stdin.readline

n,m,h = map(int,input().split())
if m == 0:
  print(0)
  exit()
graph = [[False] * n for _ in range(h)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a-1][b-1] = True


def check():
  for start in range(n):    
    idx = start
    for i in range(h):
      if graph[i][idx]:
        idx += 1
      elif idx > 0 and graph[i][idx-1]:
        idx -= 1
    if start != idx:
      return False
  return True


def bf(cnt,r,c):
  global ans
  if check():
    ans = min(cnt,ans)
    return
  elif cnt == 3 or ans < cnt:
    return

  for i in range(c,n-1):
    col = i
    for j in range(r,h):
      if not graph[j][i] and not graph[j][i+1]:
        if i+1 <= n and not graph[j][i+1]:
          graph[j][i] = True
          bf(cnt+1,j+2,i)
          graph[j][i] = False


def bf(cnt,r,c):
  global ans
  if check():
    ans = min(ans,cnt)
    return
  elif cnt ==3 or ans <= cnt:
    return

  for i in range(r, h): 
    k = c if i == r else 0 
    for j in range(k, n-1): 
      if not graph[i][j] and not graph[i][j+1]: 
        graph[i][j] = True 
        bf(cnt+1, i, j+2) 
        graph[i][j] = False
          
ans = 4
bf(0,0,0)
print(ans if ans < 4 else -1)



