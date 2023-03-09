import sys
input = sys.stdin.readline

n,t = map(int,input().split())
# k 예상 공부 시간, s 배점
data = [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (t+1)

for time,score in data:
	for i in range(t,time-1,-1):
		dp[i] = max(dp[i-time]+score, dp[i])

	print(dp)

print(dp[t])


# ans = 0
# for i in range(len(data)):
# 	for j in range(i, len(data)):
# 		time = data[i][0] + data[j][0]
# 		if time > t:
# 			continue

# 		ans = max(ans, data[i][1]+data[j][1])

# print(ans)


