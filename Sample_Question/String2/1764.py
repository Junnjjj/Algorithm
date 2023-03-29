import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]

b_dict = {}
for item in b:
	b_dict[item] = 1

c = []
for item in a:
	try:
		if b_dict[item]:	
			c.append(item)
	except:
		continue

c.sort()
print(len(c))
print('\n'.join(c))

