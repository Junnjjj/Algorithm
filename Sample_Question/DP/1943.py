import sys
input = sys.stdin.readline

def solution(sum_coin,coins):
	half_sum = sum_coin // 2
	dp = [0] * (sum_coin+1)
	dp[0] = 1
	
	for coin_detail in coins:
		coin,count = coin_detail

		for i in range(sum_coin, coin-1, -1):
			if dp[i-coin]:
				for j in range(count):
					if i + coin*j <= sum_coin:
						dp[i + coin*j] = 1

	return dp[half_sum]

result = []
for _ in range(3):
	n = int(input())
	coins = []
	sum = 0
	for _ in range(n):
		coin,count = map(int,input().split())
		sum += coin*count
		coins.append((coin,count))

	if sum&1:
		print(0)
		continue

	ans = solution(sum, coins)
	print(ans)

