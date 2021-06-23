#부품 찾기

#n 입력 받기
n = int(input())
array1 = list(map(int, input().split())) 

m = int(input())
array2 = list(map(int, input().split()))

#array1 정렬
array1.sort()

#array2 요소가 array1 에 있는지 확인

def binary_serach(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target: #target 이 왼쪽에 있으면
      end = mid -1
    else:
      start = mid + 1

  return None

for i in range(m):
  if not binary_serach(array1, array2[i], 0, len(array1) -1) == None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')

