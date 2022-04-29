# 정수 삼각형
import sys

input = sys.stdin.readline

# n = int(input())
# triangle = [list(map(int,input().split())) for _ in range(n)]

# d = [0] * (n)
# d[0] = triangle[0][0]
# temp = 0

# for i in range(1,n):
#   if triangle[i][temp] > triangle[i][temp+1]:
#     d[i] = d[i-1]+triangle[i][temp]
    
#   else:

#     d[i] = d[i-1]+triangle[i][temp+1]
#     temp += 1
    
# print(d)


n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      up_left = 0
    else:
      up_left = dp[i-1][j-1]

    if j==i:
      up = 0
    else:
      up = dp[i-1][j]

    dp[i][j] = dp[i][j] + max(up_left,up)

for item in dp:
  print(item)