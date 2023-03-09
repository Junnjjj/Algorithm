import sys

input = sys.stdin.readline

n = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))
# data = [(0,0)]
data = []
for i in range(n):
	data.append((minus[i], plus[i]))

# dp = [[0 for _ in range(101)] for _ in range(n+1)]

# result = 0
# for i in range(1,n+1):
# 	for j in range(1,100):

# 		ne,po = data[i][0], data[i][1]

# 		if j < ne:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(po + dp[i-1][j-ne], dp[i-1][j])

# 		result = max(dp[i][j], result)

# print(result)

# solution2

dp = [0] * 101
for minus, plus in data:
	for i in range(100, minus, -1):
		dp[i] = max(dp[i], dp[i - minus] + plus)

print(dp[100])
