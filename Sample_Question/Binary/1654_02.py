# BinarySearch 같은데 : 1654
import sys
input = sys.stdin.readline

k,n = map(int,input().split())
data = [int(input()) for _ in range(k)]

def solution():
	answer = 0
	start = 1
	end = max(data)

	while start <= end:
		mid = (start + end) // 2
		line_sum = 0 

		for line in data:
			line_sum += line // mid

		if line_sum >= n:
			start = mid + 1
			answer = max(answer, mid)

		else:
			end = mid - 1

	return answer

print(solution())
