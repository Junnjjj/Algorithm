import sys
input = sys.stdin.readline

def solution(arr):  
  a,b = arr[0], arr[1]
  dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
  for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
      if a[i-1] == b[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  
  print(dp[-1][-1])
  return

lst = list(input().rstrip() for _ in range(2))

solution(lst)