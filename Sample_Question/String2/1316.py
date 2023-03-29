import sys
input = sys.stdin.readline

n = int(input())

def solution(string):
	for i in range(1,len(string)):

		if string[i] == string[i-1]:
			continue

		else:
			if string[i] in string[:i]:
				return False

	return True

ans = 0
for _ in range(n):
	str = input().rstrip()
	if solution(str):
		ans += 1

print(ans)