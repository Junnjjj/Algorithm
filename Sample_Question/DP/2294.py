import sys
input = sys.stdin.readline

def solution():
	dp = [1e9] * (k+1)
	dp[0] = 0

	for coin in coins:
		for i in range(coin,k+1):
			dp[i] = min(dp[i], dp[i-coin]+1)

	print(dp)

n,k = map(int,input().split())
coins = []
for _ in range(n):
	coin = int(input())
	coins.append(coin)

solution()