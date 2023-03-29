import sys
input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

new_data = {}
for item in data:
	a = item.split('.')
	if a[1] in new_data:
		new_data[a[1]] = new_data[a[1]]+1
	else:
		new_data[a[1]] = 1


new_data = sorted(new_data.items())
for item in new_data:
	print(item[0],item[1])
print(new_data)