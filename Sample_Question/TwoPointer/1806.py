import sys

input = sys.stdin.readline

def twoPointer(arr,N,M):
  start,end = 0,1
  length = 1e9  

  while end <= N and start <= end:

    sum_arr = arr[start:end]
    total = sum(sum_arr)

    if total < M:
      end +=1
      
    elif total >= M:
      length = min(end-start,length)      
      start +=1
      

  return length

n,s = map(int,input().split())
nums = list(map(int,input().split()))

# 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
ans = twoPointer(nums,n,s)
print(ans if ans != 1e9 else 0)

