#음류수 얼려 먹기

#첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다
#두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1

#한번에 만들 수 있는 아이스크림의 개수

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  #주어진 범위 벗어나면 종료
  if x<= -1 or x >= n or y <= -1 or y >= m:    
    return False
  
  #현재 노드를 방문하지 않았다면
  if graph[x][y] == 1:
    #해당 노드를 방문 처리
    graph[x][y] = 0
    #상하좌우 재귀호출
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

#모든 노드에 대하여 음류수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i,j) == True:
      result += 1
    

print(result)