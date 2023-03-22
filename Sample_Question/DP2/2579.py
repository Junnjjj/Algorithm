import sys
input = sys.stdin.readline

n = int(input())
s = [0]
for _ in range(n):
	s.append(int(input()))

dp = [0] * (n+1)
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(dp[0]+s[2], dp[1]+s[2])

for i in range(2,n+1):
	dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

print(dp[n])