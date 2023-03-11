# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# data = []
# for _ in range(n):
# 	row = list(map(int,input().split()))		
# 	for _ in range(row[2]):
# 		data.append((row[0],row[1]))


# temp = [[] for _ in range(m+1)]

# def solution():
# 	dp = [0] * (m+1)

# 	for i,item in enumerate(data):
# 		c,s = item[0],item[1]
# 		for j in range(c,m+1):

# 			origin = dp[j] 
# 			sum = dp[j-c] + s

# 			if (c,i) not in temp[c]:
# 				if origin >= sum:
# 					dp[j] = origin					
# 				else:
# 					dp[j] = sum				
# 					temp[j] = temp[j-c]
# 					temp[j].append((c,i))

# 		print(temp)

# 	print(dp)


# solution()

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dp = [0 for _ in range(M+1)]
weight, satisfaction = [], []
for _ in range(N):
    V, C, K = map(int, input().split())

    idx = 1
    while K > 0:
        tmp = min(idx, K)

        weight.append(V * tmp)
        satisfaction.append(C * tmp)

        idx *= 2
        K -= tmp

print(weight)
print(satisfaction)
# for i in range(len(weight)):
#     for j in range(M, 0, -1):
#         if j >= weight[i]:
#             dp[j] = max(dp[j], dp[j-weight[i]] + satisfaction[i])

for i,w in enumerate(weight):
	for j in range(M,w-1,-1):		
		dp[j] = max(dp[j], dp[j-weight[i]] + satisfaction[i])

print(dp[M])