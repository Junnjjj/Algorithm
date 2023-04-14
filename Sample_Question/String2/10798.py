import sys
input = sys.stdin.readline

data = [list(input().rstrip()) for _ in range(5)]

print(data)

result = ''
for i in range(15):
	for j in range(15):
		try:
			result += data[j][i]			
		except:
			continue

print(result)