import sys
input = sys.stdin.readline

n = int(input())
A,B,C,D = [],[],[],[]
for _ in range(n):
	a,b,c,d = map(int,input().split())
	A.append(a)
	B.append(b)
	C.append(c)
	D.append(d)

dict = {}
for i in range(n):
	for j in range(n):
		temp = C[i] + D[j]


		if temp in dict:
			dict[temp] += 1
		else:
			dict[temp] = 1

ans = 0
for i in range(n):
	for j in range(n):

		temp = A[i] + B[j]

		temp = temp * -1

		if temp in dict:
			ans += dict[temp]
			
print(ans)