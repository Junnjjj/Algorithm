import sys

input = sys.stdin.readline

def twoPointer(arr,N,M):  
  start,end = 0,1
  ans = 1e9
    
  while start < N and end < N:
    tmp = arr[end] - arr[start]
    if tmp == M:
        print(M)
        exit(0)
    if tmp < M:
        end += 1
        continue
    start += 1
    ans = min(ans, tmp)

  return ans

n,m = map(int,input().split())
nums = []
for _ in range(n):
  nums.append(int(input()))

nums = sorted(nums)
result = twoPointer(nums,n,m)
print(result)


 # 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

# 정답 코드

import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = int(sys.stdin.readline().rstrip())
    arr.sort()
    left, right = 0, 1
    ans = sys.maxsize

    while left < N and right < N:
        tmp = arr[right] - arr[left]
        if tmp == M:
            print(M)
            exit(0)
        if tmp < M:
            right += 1
            continue
        left += 1
        ans = min(ans, tmp)
    print(ans)