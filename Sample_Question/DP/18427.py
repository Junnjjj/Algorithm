import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())

dp = [0] * (h+1)
dp[0] = 1

for i in range(n):
	blocks = list(map(int,input().split()))

	temp = dp.copy()		
	for b in blocks:

		for j in range(h,b-1,-1):
			temp[j] = dp[j-b] + temp[j]
		
	dp = temp
			
print(dp[h]%10007)



# dp = [[1]+[0]*h for i in range(n+1)]

# for i in range(1, n+1):
#     dp[i] = dp[i-1].copy()
#     blocks = list(map(int, input().split()))
#     for b in blocks:
#         for j in range(b, h+1):
#             dp[i][j]+=dp[i-1][j-b]
					
# print(dp[n][h]%10007)
