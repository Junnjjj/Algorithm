#재귀 함수로 구현
def binary_serach(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  #중간점의 값보다 찾고자 하는 값이 작을 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_serach(array, target, start, mid-1)
  #중간점 보다 찾고자 하는 값이 큰 경우 오른 쪽 환인
  else:
    return binary_serach(array, target, mid+1, end)

# n, target = map(int, input().split())
# #전체 원소 입력 받기
# array = list(map(int, input().split()))

# result = binary_serach(array, target, 0, n-1)10 7
# if result == None:
#   print("원소가 존재하지 않습니다")
# else:
#   print(result + 1)

#반복함수로 구현
def binary_serach2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1

  return None

n, target = map(int, input().split())
#전체 원소 입력 받기
array = list(map(int, input().split()))

result = binary_serach2(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result + 1)