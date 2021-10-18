n = int(input())

def solution(data):

  if len(data) <= 1: return data
  
  pivot = data[0]
  tail = data[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

<<<<<<< HEAD
  return solution(left_side) + [pivot] + solution(right_side)

data = []
for _ in range(n):
  data.append(input())

sortedResult = dict.fromkeys(solution(result))
result = list(sortedResult)
print("\n".join(result))
=======
print(result)

#test
>>>>>>> origin/master
