import sys
input = sys.stdin.readline

n,m = map(int,input().split())
times = [int(input()) for _ in range(n)]

start = 1
end = max(times) * m
ans = 0

while start <= end:	
	temp = 0
	mid = (start + end)//2

	for time in times:
		temp += mid//time

		if temp >= m:
			break

	if temp < m:
		start = mid + 1
	elif temp >= m:
		end = mid - 1

		ans = mid	

print(ans)
