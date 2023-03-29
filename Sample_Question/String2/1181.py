import sys
input = sys.stdin.readline

def solution(string):
	pass

	
n = int(input())
strings = []
for _ in range(n):
	str = input().rstrip()
	strings.append(str)

strings = list(set(strings))
strings.sort(key=lambda x: (len(x),x[0]))
print('\n'.join(strings))