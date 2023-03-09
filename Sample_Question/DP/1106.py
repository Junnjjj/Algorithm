# import sys
# input = sys.stdin.readline

# c,n = map(int,input().split())
# data = [(0,0)]
# for _ in range(n):
# 	cost,people = map(int,input().split())
# 	data.append((cost,people))

# dp = [[1001 for _ in range(1101)] for _ in range(n+1)]
# data.sort(key=lambda x:x[1])

# for i in range(1,n+1):
# 	for j in range(1,1101):
# 		cost,people = data[i][0],data[i][1]

# 		if i==1 and j%people == 0:
# 			dp[i][j] = (j//people)*cost
# 			continue

# 		if j < people:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			if j%people == 0:
# 				dp[i][j] = min(dp[i-1][j], (j//people)*cost)
# 			else:
# 				dp[i][j] = min(dp[i-1][j], dp[i][j-people]+dp[i][people])

# result = min(dp[n][c:])
# print(result)

import sys

input = sys.stdin.readline

c, n = map(int, input().split())
data = []

min_cost = [1e9] * (c + 100)
min_cost[0] = 0

for _ in range(n):
	data.append(list(map(int, input().split())))

data.sort(key=lambda x: x[0])

for cost, cus in data:
	for i in range(cus, c + 100):
		min_cost[i] = min(min_cost[i - cus] + cost, min_cost[i])

print(min(min_cost[c:]))
