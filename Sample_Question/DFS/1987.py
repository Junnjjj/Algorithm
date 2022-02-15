import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

r,c = map(int, input().split())
# data = [list(input().rstrip()) for _ in range(r)]
data = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]

move = [(-1,0), (0,1), (1,0) ,(0,-1)]

visited = [0] * 26
visited[data[0][0]] = 1
result = []
count = 1

def dfs(x, y, count):
  global ans
  ans = max(ans, count)

  for i in move:
    nx = x + i[0]
    ny = y + i[1]
    
    if 0 <= nx < r and 0 <= ny < c and visited[data[nx][ny]] != 1:
    
      visited[data[nx][ny]] = 1
      dfs(nx,ny,count+1)
      visited[data[nx][ny]] = 0
    
    #범위 안이면 dfs 재귀로 탐색

ans = 0
dfs(0,0, count)
# print(max(result))
print(ans)