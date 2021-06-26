#신장 트리

# #크루스칼 알고리즘(그리디 알고리즘) -> 최소 신장 트리 알고리즘

# def find_parent(parent,x):
#   if parent[x] != x:
#     return find_parent(parent, parent[x])
#   return parent[x]

# #두 원소가 속한 집합을 합치기
# def union_parent(parent, a,b):
#   a = find_parent(parent,a)
#   b = find_parent(parent,b)
#   if a<b:
#     parent[b] = a
#   else:
#     parent[a] = b

# #노드의 개수와 간선의 개수 입력받기
# v, e = map(int, input().split())
# parent = [0]*(v+1)

# #모든 간선을 담을 리스트와 최종 비용을 담을 변수
# edges = []
# result = 0

# #부모 노드 초기화
# for i in range(1, v+1):
#   parent[i] = i

# #모든 간선에 대해 입력 받기
# for _ in range(e):
#   a, b, cost = map(int, input().split())
#   edges.append((cost,a,b))

# #간선을 비용순으로 정렬
# edges.sort()

# #간선을 하나씩 확인하며
# for edge in edges:
#   cost ,a, b = edge
#   #사이클이 발생하지 않는 경우에만 집합에 포함하면서
#   if find_parent(parent, a) != find_parent(parent,b):
#     union_parent(parent,a,b)
#     result += cost

# print(result)

# #위상 정렬
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) #정점 A 에서 B로 이동가능
  indegree[b] += 1

#위상 정렬 함수
def toplogy_sort():
  result = [] #수행 결과 리스트
  q = deque()

  #처음 시작시 진입차수가 0 인 노드를 ㅠ에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  #Q가 빌 때까지 반복
  while q:
    now = q.popleft()
    result.append(now)
    #해당 원소와 연결된 노드들의 진입차수 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      #새롭게 진입차수가 0 이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

toplogy_sort()