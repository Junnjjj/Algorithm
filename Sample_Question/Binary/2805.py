import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # n 나무의 수 , m 가져가려는 나무의 길이
trees = list(map(int,input().split()))

left = 0
right = max(trees)
mid = (left+right) // 2

answer = 0
while left <= right:  
  temp = 0
  for tree in trees:
    remain = tree - mid
    if remain < 0:
      continue
    temp += remain # 가져갈수 있는 나무

  if temp >= m:
    answer = max(answer, mid)
    left = mid + 1    
    mid = (left+right) // 2
    
  elif temp < m:    
    right = mid - 1
    mid = (left + right) // 2


print(answer)
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값