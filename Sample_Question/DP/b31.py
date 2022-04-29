# 금광

import sys

input = sys.stdin.readline

d = [0] * 30001

def solution(x):
  for i in range(2, x+1):
    d[i] = d[i-1] + 1
  
    if i % 2 == 0:
      d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
      d[i] == min(d[i], d[i//2] + 1)
    if i % 5 == 0:
      d[i] == min(d[i], d[i//2] + 1)
  
  print(d[x])

n = int(input())
solution(n)
