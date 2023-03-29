import sys
input = sys.stdin.readline

n,k = map(int,input().split())
data = list(map(int,input().split()))

dp = [1e9] * n
dp[0] = 0

for i in range(n):
	for j in range(i,n):

		if i == j: continue

		if dp[i] == 1e9:
			continue
		
		power = (j-i)*(1+abs(data[i]-data[j]))
		if power <= k:
			dp[j] = power

print('YES' if dp[n-1] != 1e9 else "NO")