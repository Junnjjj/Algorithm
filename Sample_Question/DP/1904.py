import sys

input = sys.stdin.readline

n = int(input())

1 아니면 00

1 - 1
2 - 00 11
3 - 

# N인 모든 2진 수열을 만들 수 없게 되었다. 예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. (01, 10은 만들 수 없게 되었다.) 또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.

import sys

input = sys.stdin.readline
        

dp = [0] * 1000001
dp[1]=1
dp[2]=2

for i in range(3,1000001):
    dp[i]=dp[i-1]+dp[i-2]
    if dp[i]>=15746: 
        dp[i]=dp[i]%15746
    
n=int(input())
print(dp[n])