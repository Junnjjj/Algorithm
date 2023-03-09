import sys

input = sys.stdin.readline

n,k = map(int,input().split())
data = [[0,0]]
item = [list(map(int,input().split())) for _ in range(n)]
data += item


dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
	for j in range(1,k+1):
		weight = data[i][0]
		value = data[i][1]

		if j < weight:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])
	