# #팀 결성
# def find_parent(parent, x):
#   if parent[x] != x:
#     return find_parent(parent, parent[x])
#   return parent[x]

# def union_parent(parent, a, b):
#   a = find_parent(parent, a)
#   b = find_parent(parent, b)

#   if a<b:
#     parent[b] = a
#   else:
#     parent[a] = b

# #N,M 입력 받기
# n,m = map(int, input().split())
# parent = [0] * (n+1)

# for i in range(1, n+1):
#   parent[i] = i

# for _ in range(m):
#   index, a, b = map(int, input().split())

#   #합치기
#   if index == 0:
#     union_parent(parent, a, b)
#   elif index == 1: #확인
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a == b:
#       print('yes')
#     else:
#       print('no')


#도시 분할 계획 최소 신장 트리, 
def find_parent(parent,x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())

parent = [0]*(n+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 노드 초기화
for i in range(1, n+1):
  parent[i] = i

#간선과 cost 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b)) # a에서 b 까지 가는 비용이 c

#cost 순으로 정렬
edges.sort()

result = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost
    last = cost

print("유지비 : ", result - last)
  