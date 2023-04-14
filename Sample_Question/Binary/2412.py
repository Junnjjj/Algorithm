import sys
from collections import deque
input = sys.stdin.readline

n,t = map(int,input().split())
data = [[] for _ in range(t+1)]
max_x = 0
for _ in range(n):
	x,y = map(int,input().split())
	max_x = max(x,max_x)
	data[y].append(x)


def isValid(m):
	q = deque()
	visited = [[1e9]*(t+1) for _ in range(max_x+1)]	
	# 시작점
	q.append((0,0,0))
	visited[0][0] = 0	

	while q:
		x,y,temp = q.popleft()
		
		if y == t:						
			return True

		for j in (y-2,y-1,y,y+1,y+2):

			if not 0<=j<t+1:
				continue
			
			for i in data[j]:

				if abs(i-x) <= 2 and visited[i][j] > temp + 1 and temp + 1 <= mid:
					q.append((i,j,temp+1))
					visited[i][j] = temp+1

	return False
			

start = 0
end = n

ans = 0
while start <= end:
	mid = (start+end) // 2	


	if isValid(mid):
		end = mid - 1
		ans = mid
	else:
		start = mid + 1



print(ans if ans != 0 else -1)