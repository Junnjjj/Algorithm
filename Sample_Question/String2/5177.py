import re, sys
input = sys.stdin.readline

n = int(input())

# 에라토스테네스의 체 알고리즘 => 소수 판별 알고리즘 
arr = [v for v in range(n+1)]
print(arr)
for i in range(2,n+1):
  if arr[i] == 0:
    continue # 이미 지워진 수라면 건너 뛰기
  # 이미 지워진 숫자가 아니라면, 그 배수부터 출발하여 가능한 모든 숫자 지우기
  for j in range(2*i,n+1,i):    
    arr[j] = 0

# a = re.compile([a-zA-Z])

# n = int(input())
# s,e = input().rstrip().split("*")
# pt = re.compile(s+".*"+e+"+")

# for i in range(n):
# 		string = input().rstrip()
# 		a = pt.search(string)


# 		print('@@@@@@@@',a, a.group())
	
# 		if a and a.group() == string:
# 			print("DA")
# 		else:
# 			print("NE")