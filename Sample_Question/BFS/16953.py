# from collections import deque

# a, b = map(int, input().split())

# #2를 곱하고
# #1을 수의 가장 오른쪽에 추가 x * 10 + 1

# # MAX = 10 ** 9
# # 1,000,000,000  10억
# # 첫만 리스트를 10번 생성
# # 10 ** 7 
# MAX = 10 ** 7


# graph = [0] * (MAX+1)

# q = deque()
# q.append(a)

# def bfs():
#   count = 0
#   graph = [0] * (MAX+1)

#   while q:
#     x = q.popleft()
    
#     if x == b:
#       return graph[x] + 1
#       break

#     for nx in (2*x, (10*x)+1):

#       if 0<= nx <= MAX and not graph[nx]:
#         graph[nx] = graph[x] + 1
#         q.append(nx)
      
#       if nx > MAX:
#         graph = [0] * (MAX + 1)
#         count += 1 # * 10 
#         nx = nx % (10 ** 7)

        

  
#   return -1

n, m = map(int,input().split())
count = 0
while True:
    if m % 2 == 0:
        m = m / 2
    else:
        m -= 1
        m /= 10
    count += 1
    if m <= n:
        break

if m < n:
    print(-1)
else:
    print(count + 1)