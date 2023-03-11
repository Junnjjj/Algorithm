import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())

	dp = [1e9] * (1000*100)
	dp[0] = 0
	sum_a = 0
	
	for _ in range(n):
		a,b = map(int,input().split())
		sum_a += a

		for i in range(100*100, a-1, -1):
			dp[i] = min(dp[i], dp[i-a]+b)


	ans = 1e9
	for i in range(sum_a+1):
		ans = min(ans, max(sum_a-i, dp[i]))

	print(ans)