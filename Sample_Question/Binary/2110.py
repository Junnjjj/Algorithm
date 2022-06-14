import sys
input = sys.stdin.readline

n,c = map(int,input().split()) # 집의 개수, 공유기 개수
homes = list(map(int,input().split()))

left = 1
right = max(homes) - 1
mid = (left+right) // 2

homes.sort()

answer=  0
while left <= right:
  temp = 0

  for i in range(len(homes) - 1):
    distance = homes[i+1] - homes[i] # 집간의 거리
    if distance <= mid:
      temp += 1

  if temp >= c:
    if temp == c:
      answer = max(answer, mid)
    left = mid + 1
    mid = (left+right) // 2
  elif temp < c:
    right = mid - 1
    mid = (left+right) // 2  

print(answer)