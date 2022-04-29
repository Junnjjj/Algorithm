import sys

input = sys.stdin.readline

## 개미전사

# n = int(input())
# food = list(map(int,input().split()))

# d = [0] * 100

# d[0] = food[0]
# d[1] = max(food[0], food[1])
# for i in range(2,n):
#   d[i] = max(d[i-1], d[i-2]+food[i])

# for i in range(5):
#   print(d[i])
# print(d[n-1])

## 바닥 공사
# n = int(input())

# d = [0] * 1001

# d[1] = 1
# d[2] = 3
# for i in range(3, n+1):
#   d[i] = (d[i-1] + 2 * d[i-2]) % 796796

# print(d[n])

## 효율적인 화페 구성
n,m = int(input().split())
money = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    d[j] = min(d[j], d[j-array[i]] + 1)