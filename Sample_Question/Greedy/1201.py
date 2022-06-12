import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

if n < m+k-1 or n > m*k:
    print(-1)
else:
    l = list(range(k,0,-1))
    n -= k
    m -= 1
    while m:
        l.extend(range(k+n//m,k,-1))
        k += n//m
        n -= n//m
        m -= 1    
    print(*l)


# n,m,k = map(int,input().split())

# num = [v for v in range(1,n+1)]

# idx = 0
# tmp = []
# for i in range(m):
#   if idx >= n:
#     print(-1)
#     exit()
#   if i == 0:
#     tmp.append(num[:k])
#     idx = k
#   elif i == m-1:
#     tmp.append(num[idx:])
#   else:     
#     tmp.append([num[idx]])
#     idx = idx+1

    

# answer = []
# for i in range(len(tmp)):  
#   answer.extend(reversed(tmp[i]))

# if len(answer) != len(list(set(answer))):
#   print(-1)
# else:
#   print(' '.join(list(map(lambda x: str(x), answer))))
    

# # k 보다 작거나 같아야 한다 => 이걸 고쳐야하네
# # n 개를 
# # k 
# # n-k

# # 13 5 4

# # 13 - 4  = 9
# # 9 / 4 = 2
# # 4 2 2 2 2

# 13 - 3 = 10
# 10 / 4 = 2 , 2
# 3 2 2 2 2 

