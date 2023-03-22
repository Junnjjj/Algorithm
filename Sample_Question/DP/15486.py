import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i,item in enumerate(data):
	day,cost = item[0], item[1]

	if day+i <= n:
		dp[day+i] = max(dp[day+i], dp[i]+cost)

	dp[i+1] = max(dp[i+1], dp[i]) 

print(dp[n])