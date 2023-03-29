import sys
input = sys.stdin.readline

def solution(a,b):

	idx = 0

	for i in range(len(b)):
		if b[i] == a[idx]:
			idx += 1

			if idx == len(a)-1:
				return 'Yes'

	return 'No'


while True:
	try:
		a,b = map(str,input().split())
		ans = solution(a,b)
		print(ans)
	except:
		break