# 아직 못푼다

import sys
import string

input = sys.stdin.readline

temp = string.digits + string.ascii_uppercase
num_dict = {k:v for v,k in enumerate(temp)}
print(num_dict)

N = int(input())
for _ in range(N):
  string = str(input().rstrip())
K = int(input())

# 36진법 숫자(0-9, A-Z) 중에서 K개의 숫자를 고른다. 그러고 나서 N개의 수 모두에서 나타난 그 숫자를 Z로 바꾼다. 그 이후에 N개의 수를 모두 더한다.

# 이때 가능한 합의 최댓값을 구하는 프로그램을 작성하시오. 합의 최댓값도 36진수로 출력한다.

# 5
# GOOD
# LUCK
# AND
# HAVE
# FUN
# 7