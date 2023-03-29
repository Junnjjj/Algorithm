import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
loc = [list(map(int,input().split())) for _ in range(m)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(n):	
	for j in range(n):

		if i == 0 and j == 0:
			continue

		dp[i][j] = dp[i][j-1] + graph[i][j]		

for row in dp:
	print(row)

for x1,y1,x2,y2 in loc:
	x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
	if x1==x2 and y1 ==y2:
		print(graph[x1][y1])
		continue
	
	ans = 0
	if y1 == 0:
		for i in range(x1,x2+1):
			ans += dp[i][y2]		
	else:
		y1 = y1 - 1

		for i in range(x1,x2+1):
			ans += (dp[i][y2] - dp[i][y1])
		# ans = (dp[x2][y2] - dp[x2][y1]) + (dp[x1][y2] - dp[x1][y1])
		
	print(ans)
