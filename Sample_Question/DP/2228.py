import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = []
for _ in range(n):
  number = int(input())
  num.append(number)

print(num)

# d[i][j] 는 a[1] ~ a[i] 수가 있을 때 
# j 개의 구간으로 나누고 구간에 속하는 값들의 총합의 최대값

# 1. i 가 구간에 포함되지 않으면 
# d[i-1][j] => i-1 까지는 j개의 구간

# 2. i가 구간에 포함이 되었다
# d[k-2][j-1] , k부터 i 까지는 구간 1 합해서 j개의 구간