import sys
input = sys.stdin.readline

s = int(input())

if s == 1:
	print(1)
	exit()

if s == 2:
	print(1)
	exit()

sum = 0
for n in range(1,s):
	sum += n

	if sum == s:
		print(n)
		break
	if sum > s:
		print(n-1)
		break
