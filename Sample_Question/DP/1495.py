import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())
volumn = list(map(int,input().split()))


dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

ans = 0
for i in range(1,n+1):  
  v = volumn[i-1]  
  check = False    
  for idx,d in enumerate(dp[i-1]):    
    if d == 1:    
      minNum,maxNum = idx-v, idx+v      
      if 0<=minNum<=m:
        dp[i][minNum] = 1       
        check = True
        if i == n:
          ans = max(ans,minNum)        
          
      if 0<=maxNum<=m:
        dp[i][maxNum] = 1
        check = True
        if i == n:
          ans = max(ans,maxNum) 
  
print(ans if check else -1)

# 238
#  88
# 150