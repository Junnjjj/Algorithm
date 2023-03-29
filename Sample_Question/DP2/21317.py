import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
if n == 1:
	print(0)
	exit()
data = [list(map(int,input().split())) for _ in range(n-1)]
k = int(input())

q = deque()	
cur = 0
big = False
cost = 0
q.append((cur,cost,big))

ans = 1e9
while q:
	idx,c,b = q.popleft()

	if idx == n-1:
		ans = min(ans, c)

	if idx + 1 < n :
		q.append((idx+1, c+data[idx][0], b))

	if idx + 2 < n:
		q.append((idx+2, c+data[idx][1], b))

	if idx + 3 < n and not b:
		q.append((idx+3, c+k, True))

print(ans)

# dp = [1e9] * n
# dp[0] = 0


# for i,item in enumerate(data):
# 		# dp[1] 부터 채워짐
# 	small,big = item

# 	# i+1 # 작은 점프 +1 칸 에너지 small
# 	if i+1 < n:		
# 		dp[i+1] = min(dp[i]+small, dp[i+1])
		
		
# 	# i+2 # 큰 점프 + 2 칸 에너지 big
# 	if i+2 < n:		
# 		dp[i+2] = min(dp[i]+big, dp[i+2])		

# ans = dp[n-1]
# for i in range(n-1):

# 	if i+3 < n:
	
# 		bigZump_from_I_energy = dp[i] + k		
	
# 		if dp[i+3] > bigZump_from_I_energy:

# 			ans = min(bigZump_from_I_energy + (dp[n-1] - dp[i+3]), ans)

# print(ans)


# 5
# 1 2
# 2 3
# 4 5
# 6 7
# 4