#선택 정렬, Selection sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[j] < array[min_index]:
      min_index = j
  # swap
  array[i], array[min_index] = array[min_index], array[i]

print(array)
#선택정렬의 시간 복잡도 O(n^2)

#삽입 정렬, Insertion sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)


#퀵 정렬, Quick sort
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  #원소가 1개인 경우 종료
  if start >= end:
    return

  pivot = start
  left = start+1
  right = end
  while left <= right:
    #피벗보다 큰 데이터를 찾을 때 까지 반복
    while left <= end and array[left] <= array[pivot]:
      left +=1
    #피벗보다 작은 데이터를 찾을 때 까지 반복
    while right > start and array[right] >= array[pivot]:
      right -=1
    #엇갈렷다면
    if left > right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]

    #분할 종료 후 왼쪽, 오른쪽 부분 퀵 정렬 실시
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0 ,len(array)-1)
print(array)

#퀵정렬 ver_2
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))