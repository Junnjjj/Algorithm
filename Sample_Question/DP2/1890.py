import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1


for i in range(n):
	for j in range(n):
		if dp[i][j] == 0:
			continue
			
		cost = graph[i][j]
		if cost == 0:
			continue
		
		if cost+j < n:
			dp[i][cost+j] += dp[i][j]

		if cost+i < n:
			dp[cost+i][j] += dp[i][j]

		if cost+i == n-1 and cost+j == n-1:
			print(i,j,cost)

for row in dp:
	print(row)
	
# 4
# 2 3 3 1
# 1 2 1 3
# 1 2 3 1
# 3 1 1 0

