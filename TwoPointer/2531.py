import sys

input = sys.stdin.readline

def twoPointer(arr,N,K,C):
  # k 연속해서 먹는 접시의 수
  # C 쿠폰 번호
  left,right = 0,K
  count = 0

  while right < len(arr):

    k_size = arr[left:right]

    if C in k_size: # 쿠폰스시가 배열에 있을 경우
      # 다음 스시 하나를 먹을 수 있음
      if arr[right] not in k_size:
        count = max(count, len(set(k_size))+1)
      else:
        count = max(count,len(set(k_size)))
    elif C not in k_size: # 쿠폰스시 하나를 만들어줌
      count = max(count,len(set(k_size))+1)

    left +=1
    right +=1
        
  print(count)

# 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]

sushi = sushi + sushi[:k+1] # 회전까지 고려
twoPointer(sushi,n,k,c)

# 2 2 2 2
# 1
# 1

# 2

# 6 6 6 6
# 1
# 2
# 3
# 4
# 5
# 6

# 6