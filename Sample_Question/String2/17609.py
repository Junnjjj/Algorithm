import sys
input = sys.stdin.readline

# 회문이면 0, 유사회문이면 1, 그 외는 2
# 한문자를 삭제 했을때 회문이면 = 유사회문

def solution(string,check):

	start = 0
	end = len(string)-1		

	while start < end:
		if string[start] == string[end]:
			start += 1
			end -= 1
		else:

			if not check:
				return 2
				
			# print(string[start:end+1])
			if solution(string[start+1:end+1], False) == 0:
				return 1

			if solution(string[start:end], False) == 0:
				return 1
						
			return 2

	return 0

n = int(input())
for _ in range(n):
	string = input().rstrip()

	print(solution(string,True))