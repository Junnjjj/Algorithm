import sys
input = sys.stdin.readline

n,k = map(int,input().split())
s = list(map(int,input().split()))

for i in range(n):
	if s[i] % 2 == 0:
		s[i] = 1 
	else:
		s[i] = 0

ans = 0
for i in range(n):
	remain = k
	arr = 0
	for j in range(i,-1,-1):
		
		if s[j] == 1:
			arr += 1
		else:
			if remain > 0:
				remain -= 1
			else:
				break

	ans = max(ans, arr)

print(ans)