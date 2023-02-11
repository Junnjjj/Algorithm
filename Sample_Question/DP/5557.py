import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*21 for _ in range(n)]
dp[0][nums[0]] = 1

for i in range(1,n-1):
  suffix = nums[i]  
  # print(suffix)
  # print(dp[i-1])
  
  for idx,num in enumerate(dp[i-1]):

    if num != 0:
      count = dp[i-1][idx]  
      plus,minus = idx+suffix, idx-suffix      

      if 0 <= plus <= 20:
        if dp[i][plus] == 0:
          dp[i][plus] = count    
        else:
          dp[i][plus] = count + dp[i][plus]

      if 0 <= minus <= 20:        
        if dp[i][minus] == 0:
          dp[i][minus] = count    
        else:
          dp[i][minus] = count + dp[i][minus]        
  # print(dp[i])
  # print()
        
print(dp[n-2][nums[-1]])

# for item in dp:
#   print(item)
# print(dp[n-2])
      
      

# 중간에 나오는 수가 모두 0 이상 20 이하
# 음수는 안되고 20 넘으며 ㄴ안됨

# 마지막 값이 8 이 나오는 수여야함
# + -


# 11
# 8 3 2 4 8 7 2 4 0 8 8

# 10