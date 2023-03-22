import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))


dp = [0] * (n)
dp[0] = 1

ans = 0
for i in range(1,n):
	temp = 0
	for j in range(i):

		if data[j] < data[i]:

			if dp[j] > temp:
				temp = dp[j]

	dp[i] = temp+1

print(max(dp))


# 11
# 10 20 50 30 40 50 20 30 40 50 60
# 10 20    30 40 50 