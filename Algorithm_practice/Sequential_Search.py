def sequential_search(target, array):
  n = len(array)

  for i in range(n):
    if array[i] == target:
      return i + 1

#n  and target
target = input()

array = input().split()

print(sequential_search(target, array))