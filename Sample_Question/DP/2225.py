import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(k+1):
	for j in range(n):
		if i == 1:
			dp[i][j] = 1

		if j == 0:
			dp[i][j] = 1
		

for i in range(1,n+1):
	dp[k][i] = dp[k][i-1] + (k-1) + (k-2)*(i-1)

print(dp)

print(dp[k][n])