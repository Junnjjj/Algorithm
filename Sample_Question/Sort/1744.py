import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline().strip()) for _ in range(n)]

array.sort(reverse=True)

pos_array = list(filter(lambda x : x>0 , array))
neg_array = list(filter(lambda x : x<=0 , array))
neg_array.sort()

def solution(data):
  index = 1e9
  
  array_size = len(data)
  result = 0

  for i in range(array_size):
    if i == index: continue

    if i+1 == array_size:
      result += data[i]
      break
    elif data[i+1] == 1:
      result += data[i] + data[i+1]
      index = i+1
      continue 
    
    result += data[i] * data[i+1]
    index = i+1

  return result


print(solution(pos_array) + solution(neg_array))
