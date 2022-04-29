# 이친수 구하기
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

if n == 1 or n == 2:
  print(1)
  exit()
elif n== 3:
  print(2)
  exit()
  
for i in range(4,n+1):
  dp[i] = (dp[i-1] * 2) + 1

print(dp[n])

# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

  # dp
  # 1 2 3 4 5
  # 1 1 2 
  # 101
  # 100

  # 1010
  
  # 1000
  # 1001

  # (2*n)+1
  
