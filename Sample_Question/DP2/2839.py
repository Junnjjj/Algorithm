import sys
input = sys.stdin.readline

n = int(input())

if n == 4:
	print(-1)
	exit()
if n == 5 or n == 3:
	print(1)
	exit()

dp = [1e9] * (n+1)
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
	dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)

print(dp[n] if dp[n] != 1e9 else -1)