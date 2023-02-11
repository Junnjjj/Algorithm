import sys
input = sys.stdin.readline

n = int(input())
string = list(str(input().rstrip()))

open = ['(','{','[']
close = [')','}',']']

d = [[-1] * (n) for _ in range(n)]

def go(i,j):
  if i > j :
    return 1
    
  if d[i][j] != -1:
    return d[i][j]
    
  ans = 0
  for k in range(i+1,j+1,2):
    for l in range(3):
      if string[i] == open[l] or string[i] == '?':
        if string[k] == close[l] or string[k] == '?':
          temp = go(i+1,k-1) * go(k+1,j)          
          ans += temp          

  d[i][j] = ans
  return ans


ans = go(0,n-1)
print(str(ans)[-5:])


# print(string)

# 10
# (?([?)]?}?

# d[i][j] = d[i+1][k-1] * d[k+1][j]

# () {} []

# 올바른 규칙 
# 빈 문자열은 올바른 괄호 문자열이다.
# A가 올바른 괄호 문자열이라면, (A), [A], {A}도 올바른 괄호 문자열이다.
# A와 B가 올바른 괄호 문자열이라면, AB도 올바른 괄호 문자열이다.