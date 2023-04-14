import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

start,end = 0,max(data)

def validation(v):

	cnt = 1
	min_v,max_v = data[0],data[0]
	
	for i in range(1,n):
		min_v = min(min_v, data[i])
		max_v = max(max_v, data[i])

		if max_v - min_v > v:
			cnt += 1
			min_v, max_v = data[i],data[i]

	return cnt <= m

ans = 0
while start <= end:
	mid = (start+end)//2	

	if validation(mid):
		end = mid-1
		ans = mid
	else:
		start = mid+1

print(ans)