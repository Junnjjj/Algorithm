# Divide and Conquer
import sys
input = sys.stdin.readline

def solve(arr, num):
  divide = N // num
  
  new_arr = []
  for i in range(divide):
    temp = sorted(arr[i*num:(i+1)*num])    
    new_arr += temp

  if divide == K:
    print(*new_arr)
    return
    
  solve(new_arr, num*2)

N = int(input())
chickens = list(map(int,input().split()))
K = int(input())

solve(chickens, 2)