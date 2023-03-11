import sys

input = sys.stdin.readline

result = []
while True:
	n, m = map(float, input().split())
	n, m = int(n), int(m * 100)
	if n == 0 and m == 0:
		break

	data = []
	for _ in range(n):
		c, p = map(float, input().split())
		c, p = int(c), int(p * 100)
		data.append((c, p))

	dp = [0] * (m + 1)
	
	for ca, mo in data:		
		for i in range(mo,m+1):
			dp[i] = max(dp[i - mo] + ca, dp[i])			

	print(dp[m])
