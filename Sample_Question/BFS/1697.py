# from collections import deque

# n,k = map(int,input().split())
# MAX = 10 ** 5
# graph = [0] * (MAX + 1)

# # def bfs():
# #   q = deque()
# #   q.append(n) 
# #   while q:
# #     x = q.popleft()
# #     if x == k:
# #       print(graph[x])
# #     for nx in (x+1, x-1, 2*x):
# #     #범위 안이면
# #       if 0 <= nx <= MAX and not graph[nx]:
# #         q.append(nx)
# #         graph[nx] = graph[x] + 1
# # bfs()

# def bfs():
#   q= deque()
#   q.append(n)
#   while q:
#     print(q)
#     x = q.popleft()
#     if x == k:
#       print(graph[x])
#       break
#     for nx in (x+1, x-1, 2*x):
#     #범위 안이면
#       if 0 <= nx <= MAX and not graph[nx]:
#         q.append(nx)
#         graph[nx] = graph[x] + 1
# # bfs()

# test = [0,0,0]
# if test[1]:
#   print('xx')

# if not test[1]:
#   print('3')



