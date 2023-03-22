import sys
input = sys.stdin.readline

n = int(input())
dp = [1e9] * (n+1)
dp[1] = 0

for i in range(1,n+1):

	if i*3 <= n:
		dp[i*3] = min(dp[i*3], dp[i]+1)

	if i*2 <= n:
		dp[i*2] = min(dp[i*2], dp[i]+1)

	if i+1 <= n:
		dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[n])

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.