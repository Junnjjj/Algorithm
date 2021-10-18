from math import gcd

n = int(input())

data = list(map(int, input().split()))

data.sort() #정렬

def solution(arr):
  def lcm(x,y):
    return x * y // gcd(x,y)

  while True:
    arr.append(lcm(arr.pop(), arr.pop()))
    if len(arr) == 1:
      return arr[0]

print(solution(data))

