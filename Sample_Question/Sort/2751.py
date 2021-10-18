import sys

n = int(sys.stdin.readline())

def solution(data):

  if len(data) <= 1: return data
  
  pivot = data[0]
  tail = data[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return solution(left_side) + [pivot] + solution(right_side)


data = [int(sys.stdin.readline().strip()) for _ in range(n)]

result = solution(data)

for i in range(len(result)):
  print(result[i])