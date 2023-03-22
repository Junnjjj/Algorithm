import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]


for idx in range(1,n+1):
	# 치즈버거 , 감자튀김 => x,y
	x,y = map(int,input().split())

	for i in range(1, m+1):
		for j in range(1, k+1):
			if x <= i and y <= j:
				dp[idx][i][j] = max(1+dp[idx-1][i-x][j-y], dp[idx-1][i][j])

			else:
				dp[idx][i][j] = dp[idx-1][i][j]

print(dp[n][m][k])
	 
# print(dp)
# 4 3 4