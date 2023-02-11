# import sys
# from collections import deque
# input = sys.stdin.readline

# def go(start):
#   if start > len(graph):
#     return False
  
#   q = deque()
#   visited = [False] * (n+1)
#   q.append(start)  
#   visited = set()
#   visited.add(start)
#   answer = []

#   while q:
#     node = q.popleft()    

#     for m in graph[node]:      
#       toLocate, dist = m[0],m[1]

#       if dist >= start and toLocate not in visited:
#         visited.add(toLocate)
#         q.append(toLocate)

#   return True if e in visited else False
      
      
# n,m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#   a,b,c = map(int,input().split())
#   graph[a].append((b,c))
#   graph[b].append((a,c))
# s,e = map(int,input().split())

# min,max = 1,1000000000
# result= min
# while min <= max:
#   mid = (min + max) // 2
#   if go(mid):
#     result = mid
#     min = mid + 1
#   else:
#     max = mid - 1

# print(result)

# go(s,e)

# # 3 3
# # 1 2 2
# # 3 1 3
# # 2 3 2
# # 1 3

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = [[] for _ in range(n+1)]

# 각 도시의 연결여부와 무게제한을 저장하는 배열 생성
for _ in range(m):
    y, x, w = map(int, sys.stdin.readline().split())
    maps[y].append((x,w))
    maps[x].append((y,w))
# 시작점, 끝점    
start, end = map(int, sys.stdin.readline().split())

# 통과할 수 있는 무게의 최솟값 / 최댓값을 지정한다. 문제에서 정해져 있다.
_min, _max = 1, 1000000000

def bfs(c):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    result = []
    while queue:
        y = queue.popleft()
        for x, w in maps[y]:
            # 갈 수 있는 곳이면서 무게 제한에 걸리지 않을 경우
            if x not in visited and w >= c:
                visited.add(x)
                queue.append(x)
    # 도착지점을 방문할 수 있는 경우면 True, 아니면 False 반환
    return True if end in visited else False

# 이분탐색으로 최댓값을 찾는다.
result = _min
while _min <= _max:
    mid = (_min + _max) // 2
    # 해당 무게로 start -> end까지 도착이 가능한 경우
    # 값을 저장하고, 최댓값을 구하기 위해 _min 값을 올린다.
    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(result)