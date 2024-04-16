import sys
input = sys.stdin.readline

n,c = map(int,input().split())
data = list(map(int,input().split()))

if c in data:
	print(1)
	exit()

data.sort()
for i in range(n-2):
	fixed = data[i]
	left = i+1
	right = n-1
	
	while left < right:
		value = c - fixed
		
		sum = data[left] + data[right]

		if sum == value:
			print(1)
			exit()			
			
		if sum == c or fixed+data[left] == c or fixed+data[right] == c:
			print(1)
			exit()

		if value < 0:
			temp = c
			if sum > temp:
				right -= 1
			else:
				left += 1
				
		else:		
			if sum > value:
				right -= 1
			else:
				left += 1

print(0)
		