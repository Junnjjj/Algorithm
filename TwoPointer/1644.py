import sys

input = sys.stdin.readline

n = int(input())


# 에라토스테네스의 체 알고리즘 => 소수 판별 알고리즘 
arr = [v for v in range(n+1)]
for i in range(2,n+1):
  if arr[i] == 0:
    continue # 이미 지워진 수라면 건너 뛰기
  # 이미 지워진 숫자가 아니라면, 그 배수부터 출발하여 가능한 모든 숫자 지우기
  for j in range(2*i,n+1,i):    
    arr[j] = 0

prime_arr = [arr[i] for i in range(2,n+1) if arr[i] != 0]
# + 투 포인터 알고리즘
start, end = 0,1
count = 0
m = len(prime_arr)
while end <= m and start <= end:

  sum_nums = prime_arr[start:end]  
  total = sum(sum_nums)

  if total == n:    
    count +=1
    end +=1
  elif total < n:
    end +=1
    
  elif total > n:
    start += 1

print(count)