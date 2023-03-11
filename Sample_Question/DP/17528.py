import sys
input = sys.stdin.readline

n = int(input())
data = []
sum_a = 0
dp = [1e9] * ((251*251))
dp[0] = 0

for _ in range(n):
	a,b = map(int,input().split())
	sum_a += a
	data.append((a,b))
	for i in range(250*250, a-1, -1):
		dp[i] = min(dp[i], dp[i-a]+b)

	print()
	print(dp[:9])
	dp[7] = dp[7-5] + 3
	a 가 7 시간 만큼 일하지 않았을 떄 b가 일한시간 (3 + 3)
	dp[5] = min(dp[5], dp[5-5] + 3)
	a 가 5 시간 만큼 일하지 않았을 때 b가 일한 시간 3

ans = 1e9
for i in range(sum_a+1):
	ans = min(ans,max(sum_a-i, dp[i]))

print(ans)

# data = [list(map(int,input().split())) for _ in range(n)]
