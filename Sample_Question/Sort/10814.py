n = int(input())

data = []
for i in range(n):
  data.append(list(input().split()))

data.sort(key=lambda x : int(x[0]))

for i in range(len(data)):
  print(data[i][0] + " " + data[i][1])
