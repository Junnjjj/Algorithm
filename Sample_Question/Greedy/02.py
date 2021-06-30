#곱하기 혹은 더하기

#데이터 입력 받기
numbers = list(map(int, input()))

size = len(numbers)

result = numbers[0]
for i in range(1,size):
  if numbers[i] != 0 and result != 0:
    result = result * numbers[i]
  else:
    result += numbers[i]
  
print(result)
  
