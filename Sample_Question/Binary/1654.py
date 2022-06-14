import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lines = [int(input()) for _ in range(k)]

left = 1
right = max(lines)
mid = (left+right)//2

answer = 0
count = len(lines)
while left <= right:
  temp = 0
 
  for line in lines:
    temp += (line // mid)

  if temp >= n:
    answer = max(answer,mid)
    left = mid + 1
    mid = (left + right) // 2
  elif temp < n:
    right = mid - 1
    mid = (left + right) // 2

print(answer)
# 최대값 