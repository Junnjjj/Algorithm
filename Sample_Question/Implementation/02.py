#문자열 재정렬
import string

data = input()

result = 0
value = []
for i in range(len(data)):
  if data[i].isalpha():
    value.append(data[i])
  else:
    result += int(data[i])

value.sort()

print(''.join(value),result)