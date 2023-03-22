import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

temp = [data[0]]

def lower_bound(arr, item):
	start = 0
	end = len(arr)-1

	while start < end:
		mid = (start+end) // 2
		if arr[mid] >= item:
			end = mid
		else:
			start = mid + 1

	return end

for i in range(1,n):

	if temp[-1] < data[i]:
		temp.append(data[i])

	else:
		idx = lower_bound(temp, data[i])
		temp[idx] = data[i]
	

print(len(temp))