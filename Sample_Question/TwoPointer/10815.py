import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))

m = int(input())
card2= list(map(int,input().split()))

dict = {}
for i in card:
	dict[i] = True

result = []
for i in card2:
	try:
		dict[i]
		result.append('1')
	except:
		result.append('0')

print(' '.join(result))

# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10