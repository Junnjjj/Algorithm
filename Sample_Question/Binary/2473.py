import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

# Two Pointer 로 풀이
data.sort()


res = 1e9 + 1
can_result = []
for i in range(n-2):
	fixed = data[i]
	left = i+1
	right = n-1

	while left < right:
		temp = fixed + data[left] + data[right]

		if abs(temp) <= abs(res):
			can_result = [fixed, data[left], data[right]]
			res = temp
			
		
		if temp > 0:
			right -= 1
		elif temp < 0:
			left += 1
		else:
			print(fixed,data[left],data[right])
			exit()
			
print(*can_result)