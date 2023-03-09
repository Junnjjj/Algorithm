import sys
input = sys.stdin.readline

def solution(n,coins,m):
	dp = [0] * (m+1)
	dp[0] = 1

	for coin in coins:
		for i in range(m+1):

			if i >= coin:
				dp[i] += dp[i-coin]

	return print(dp[m])
	

t = int(input())
for _ in range(t):
	n = int(input())
	coins = list(map(int,input().split()))
	m = int(input())

	solution(n,coins,m)