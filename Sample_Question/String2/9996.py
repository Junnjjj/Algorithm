import re, sys
input = sys.stdin.readline
n = int(input())
s,e = input().rstrip().split("*")
pt = re.compile(s+".*"+e+"+")

for i in range(n):
		string = input().rstrip()
		a = pt.search(string)


		print('@@@@@@@@',a, a.group())
	
		if a and a.group() == string:
			print("DA")
		else:
			print("NE")