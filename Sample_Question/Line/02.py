# from collections import deque

# def solution(n, times):
    
#     if n == 2:
#         return times[0]

#     # n 을 만들어야한다
#     q = deque()
#     q.append((2,times[0])) # 처음에는 무조건 두 줄로 만들어야 한다.
#     visited = [1e9]*(n+1)
#     visited[2] = times[0]

#     while q:
#         count,cost = q.popleft()
#         print(count,cost)

#         for i,time in enumerate(times): # 현재 줄을 다 나눠본다 
            
#             # 해당 방식으로 나눌 수 있는 방법
#             size = count//(i+1)
#             if size == 0:
#                 continue

#             divide = count
#             cost_ = cost 
#             for j in range(size):
#                 # divide = divide - (i+1) + (2*(i+1))
#                 divide = divide + (i+1)
#                 cost_ = cost_ + time

#                 if divide <= n and cost_ < visited[divide]:
#                     visited[divide] = cost_
#                     q.append((divide,cost_))     

#     answer = visited[n]           
  
#     print(visited)
#     print(answer)

    
#     return answer

# N = 5
# t = [2, 4, 5]	


# N = 4
# t = [2, 3]

# solution(N,t)

print(3.21<3.1)