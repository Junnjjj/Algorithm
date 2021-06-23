#떡볶이 떡 만들기

n , m = map(int, input().split())
array = list(map(int, input().split()))

#Sequential Search
# array.sort(reverse = True)

# while True:
#   result = 0
#   for i in range(len(array)):
#     if array[i] > index:
#       result += array[i] - index

#   if result >= m: break
#   index -= 1


# print(index)
  

#Binary Search
start = 0
end = max(array)

while start <= end:
  mid = (start + end) // 2
  total = 0
  for x in array:
    if x > mid:
      total += x - mid
  
  #떡의 양이 부족한 경우
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)