import sys
input = sys.stdin.readline

# def solution(n, data):
# 	pass

n = int(input())
data = list(map(int,input().split()))

dp = [1e9] * (n)
dp[0] = 0
for i in range(1,n):
	for j in range(i):

		temp = (i-j) * (1+abs(data[i]-data[j]))
		dp[i] = min(dp[i], max(dp[j], temp))
# for i in range(n-1):
# 	for j in range(i+1,n):

# 		dp[j] = min(dp[j], (j-i) * (1 + abs(data[j]- data[i])))
		
print(dp)
print(dp[-1])


# 5000 * 5000
# 25,000,000
# 5
# 1 4 1 3 1

# (j-i) * (1 + abs(data[j]-data[i]))

