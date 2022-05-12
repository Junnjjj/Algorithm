import sys
input = sys.stdin.readline

INF = int(1e9)

def flody():
  # 점화식에 따라 플로이드 워셜 알고리즘 수행
  for k in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])      

def solution():
  answer = INF
  for start in range(1,n+1):
    max_time = 0
    
    for From in range(1,n+1):
      for To in range(1,n+1):
        edge_len = temp[From][To]
  
        if edge_len != -1:        
          remain_len = edge_len - (graph[start][To] - graph[start][From])
  
          if remain_len > 0:
            spent_time = (remain_len/2) + graph[start][To]
            max_time = max(spent_time, max_time)
              
    answer = min(max_time, answer);
  return answer


n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
temp = [[-1] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = min(graph[a][b], c)
  graph[b][a] = graph[a][b]
    
  temp[a][b] = max(temp[a][b], c)
  temp[b][a] = temp[a][b]

  
flody()
ans = solution()
print(round(ans,1))


