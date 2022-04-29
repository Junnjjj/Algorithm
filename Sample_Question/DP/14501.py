import sys

input = sys.stdin.readline

n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]

d = [0] * (n+1)
max_value = 0

for i in range(n-1, -1, -1):
  time = info[i][0] + i

  if time <= n:
    d[i] = max(info[i][1]+d[time], max_value)
    max_value = d[i]
  else:
    d[i] = max_value

print(d)
print(max_value)