import sys
input = sys.stdin.readline

n,k = map(int,input().split())


start = 0
end = k // 2

while start <= end:
	# mid = (start+end)//2
	mid = start + (end - start) // 2
	temp = (mid+1)*(n-mid+1)
	if temp == k:
		print('YES')
		exit()
		break

	if temp > k:
		end = mid-1
	else:
		start = mid+1

print('NO')