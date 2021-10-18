n = int(input())
data = list(map(int, input().split()))
array = []
for i, x in enumerate(data):
  array.append((i+1,x))

array.sort(key = lambda x : x[1])

result = 0
for i in range(len(array)):
  result += array[i][1]* (len(array) - i)

print(result)