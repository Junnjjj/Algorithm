import sys
input = sys.stdin.readline


MAX = 10000001
n,m = map(int,input().split())
data = []
a = list(map(int,input().split()))
b = list(map(int,input().split()))
new_m = sum(a)

for i in range(n):
	data.append((a[i],b[i]))

def solution():
	dp = [MAX] * (new_m+1)
	dp[0] = 0

	data.sort(key=lambda x:x[0])
	print(data)


	for mem,cost in data:
		# for i in range(mem,new_m+1):
		# 	dp[i] = min(dp[i], dp[i-mem] + cost)
		for i in range(new_m, mem-1, -1):
			dp[i] = min(dp[i], dp[i-mem]+cost)
				
	print(min(dp[m:]))

solution()