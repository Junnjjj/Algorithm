import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
	g = int(input())
	data.append(g)

dp = [0] * n
dp[0] = data[0]
if n == 1:
	print(dp[0])
	exit()

dp[1] = dp[0] + data[1]

if n == 2:
	print(dp[1])
	exit()
	
dp[2] = max(dp[0] + data[2], data[1]+data[2])

if n == 3:
	print(max(dp[1],dp[2]))
	exit()

# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.


for i in range(3,n):	
	temp = dp[i-3] if not dp[:i-2] else max(dp[:i-2])
	dp[i] = max(max(dp[:i-1]) + data[i] , temp + data[i-1] + data[i])

print(dp)
print(max(dp))

# 4
# 10
# 10
# 1
# 0

# 5
# 10 
# 3 
# 10 
# 3 
# 11