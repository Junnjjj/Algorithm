import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
for _ in range(n):
  num = int(input())
  coin.append(num)

count = 0

for c in reversed(coin):
  count += k//c
  k = k%c

print(count)

# 4200 840 420 84 42 