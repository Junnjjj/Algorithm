import sys

input = sys.stdin.readline

n = int(input())
solider = list(map(int,input().split()))
solider.reverse()

dp = [1] * n

for i in range(1,n):
 for j in range(0,i):
   if solider[j] < solider[i]:
     dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))
  