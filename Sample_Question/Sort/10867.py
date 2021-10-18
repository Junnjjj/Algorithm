
n = int(input())

data=list(map(int, input().split()))

data = list(dict.fromkeys(data))
data.sort()
for x in data:
  print(x, end=' ')
  