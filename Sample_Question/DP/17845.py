import sys
input = sys.stdin.readline


#  n 최대 공부 시간
# data (x,y) 중요도, 공부 시간

def solution():
	dp = [0] * (n + 1)

	for im, time in data:
		for i in range(n, time - 1, -1):
			dp[i] = max(dp[i - time] + im, dp[i])

	print(dp[n])


n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(k)]

solution()
