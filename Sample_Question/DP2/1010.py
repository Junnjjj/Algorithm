import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n,m = map(int,input().split())

	ans = 1	
	dp = [0] * (m+1)
	dp[0] = 1
	dp[1] = 1
	for i in range(2,m+1):
		dp[i] = dp[i-1] * i
	
	ans = dp[m] // (dp[n] * dp[m-n])
	print(ans)
