import sys
input = sys.stdin.readline

def solution(n,data):
	dp = [[0]*n for _ in range(2)]

	dp[0][0],dp[1][0] = data[0][0], data[1][0]
	if n == 1:
		print(max(dp[0][0], dp[1][0]))
		return
	dp[0][1],dp[1][1] = dp[1][0] + data[0][1], dp[0][0] + data[1][1]
	if n == 2:
		print(max(dp[0][1], dp[1][1]))
		return
	
	ans = 0
	for i in range(2,n):
		for j in range(2):
			val = data[j][i]

			k = 0 if j == 1 else 1
			dp[j][i] = max(dp[j][i-2]+val, dp[k][i-2]+val, dp[k][i-1]+val)

			ans = max(ans,dp[j][i])
	print(ans)

t = int(input())
for _ in range(t):
	n = int(input())
	data = [list(map(int,input().split())) for _ in range(2)]

	solution(n,data)