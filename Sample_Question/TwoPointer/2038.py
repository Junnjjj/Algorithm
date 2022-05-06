# 골롱수열
import sys

input = sys.stdin.readline

n = int(input())

# 모든 k에 대해 k가 수열상에서 f(k)번 등장하는 단조증가 수열이다. 단조증가 수열이란 k값이 증가함에 따라 f(k)값이 감소하지 않는 수열을 말한다. 여기서 k와 f(k)는 모두 자연수이다.

g = [0] * (11111111)

g[1] = 1
now = 1
idx = 1
while now < n:
  idx += 1
  g[idx] = 1 + g[idx - g[g[idx-1]]]
  now += g[idx]

print(idx)
