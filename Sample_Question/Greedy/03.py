#문자열 뒤집기

data = list(map(int, input()))

print(data)

zero = 0
one = 0
index = data[0]
for i in range(1,len(data)):
  if data[i] != index and index == 1:
    zero += 1
    index = data[i]
    continue
  else:
    one += 1
    index = data[i]

if zero < one:
  print(zero)
else:
  print(one)
  