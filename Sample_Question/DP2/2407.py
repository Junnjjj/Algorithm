import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
	dp[i] = i*dp[i-1]

ans = dp[n] / (dp[m] * dp[n-m])
print(int(ans))
# n!/r! * (n-r)!