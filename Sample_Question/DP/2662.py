import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = []
dp = [[0]*m for _ in range(n+1)]
for _ in range(n):
	row = list(map(int,input().split()))
	data.append(row[1:])


for i in range(1,n+1):
	for j in range(m):
		val = 0
		for k in range(1,n):
			for t in range(1,n):
				if k+t == i:	
					if i==2: 
						print(k,t,i)
					val = max(val, data[k][j]+data[t][j])		
					
		dp[i][j] = max(val, max(data[i-1]))

print(dp)
	