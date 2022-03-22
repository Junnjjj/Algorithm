import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

result = []
for _ in range(t):
  definition = input().rstrip('\n')
  if 'RR' in definition:
    definition=definition.replace('RR', '')
  
  n = int(input())

  numbers = input().rstrip()
  numberList = deque()
  if ',' not in numbers:
    if len(numbers) == 2 and 'D' in definition:
      result.append('error')
      continue
    numberList.append(numbers[1:-1])    
  else:
    numberSplit = numbers.split(',')      
    for i,item in enumerate(numberSplit):
      if i == 0:
        numberList.append(item[1:])
      elif i == len(numberSplit) - 1:
        numberList.append(item[:-1])
      else:
        numberList.append(item)  

  reverse = False  
  check1 = False
  
  for o in definition:      
    if o == 'R': # 배열을 뒤집기
      reverse = True if reverse == False else False      
          
    elif o == 'D': # 앞에 버리기      
      if not numberList:
        check1 = True
        break
      if reverse: # 뒤집혔을 경우
        numberList.pop()
      else:
        numberList.popleft()

  if check1:
    result.append('error')
    continue
    

  if reverse: numberList.reverse()
  str = '['     
  for i,x in enumerate(numberList):
    if i == 0:
      str += x
    else:
      str = str + ',' + x
  str = str+']'
  result.append(str)    
  
print("\n".join(result))

# 1
# D
# 0
# []

# 1
# DDDD
# 4
# [1,2,3,4]
