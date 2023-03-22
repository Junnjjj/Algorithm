import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))


dp = [0] * (n)
dp[n-1] = 1

ans = 0
for i in range(n-2,-1,-1):
	temp = 0
	for j in range(i+1,n):

		if data[j] < data[i]:

			if dp[j] > temp:
				temp = dp[j]

	dp[i] = temp+1

print(dp)
print(max(dp))