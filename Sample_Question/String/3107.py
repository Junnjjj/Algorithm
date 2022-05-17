import sys

input = sys.stdin.readline

ip = str(input().rstrip())

def makeOrigin(arr):
  newArr = []
  for i in range(len(arr)):
    if len(arr[i]) != 4:
        temp = '0'*(4-len(arr[i]))
        newArr.append(temp+arr[i])
    else:
      newArr.append(arr[i])
  return newArr

if '::' in ip:
  origin_ip = []
  left,right = ip.split('::')  

  if len(left) == 0:    
    right = right.split(':')
    for i in range(8-len(right)):
      origin_ip.append('0000')    
    origin_ip += makeOrigin(right)
  elif len(right) == 0:
    left = left.split(':')
    origin_ip += makeOrigin(left)
    for i in range(8-len(left)):
      origin_ip.append('0000')
  else:
    right = right.split(':')
    left = left.split(':')
    origin_ip += makeOrigin(left)    
    for i in range(8-(len(left)+len(right))):
      origin_ip.append('0000')   
    origin_ip += makeOrigin(right)    
      
else:
  ip_list = ip.split(':')
  origin_ip = []
  origin_ip += makeOrigin(ip_list)  
      
print(':'.join(origin_ip))