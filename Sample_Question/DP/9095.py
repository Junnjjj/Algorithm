import sys

input = sys.stdin.readline

# 1, 2, 3 의 합으로 나타낼 수 있는 방법의 수


def solution(num):

  for i in range(4,num+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

  return d[num]

ans = []
t = int(input())
for _ in range(t):
  n = int(input())
  d = [0] * (n+1)
  if n<4:
    if n == 1:
      ans.append(1)
    elif n == 2:
      ans.append(2)
    else:
      ans.append(4)
    continue
    
  d[1],d[2],d[3] = 1,2,4

  ans.append(solution(n))

for item in ans:
  print(item)
  

  
  

# 4 를 1,2,3 의 합으로 나타내는 방법은 총 7개
# 1 1 1 1

# 1 2 3 4
# 1 1 1

# 4 - 1 = 3
# 4 - 2 = 2
# 4 - 3 = 1

# tn = d[t-1] + d[t-2] + d[t-3]

