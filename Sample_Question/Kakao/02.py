# from collections import deque
# import copy

# def twoPointer(arr1,arr2,N):
#     arr1_pointer, arr2_pointer = 0,0
#     count = 1e9

#     arr1_total = sum(arr1)
#     arr2_total = sum(arr2)

#     arr1_sum,arr2_sum = arr1_total, arr2_total

#     while True:
#         print(arr1_pointer,arr2_pointer, arr1_sum,arr2_sum)

#         # arr1_move = sum(arr1[:arr1_pointer])
#         # arr2_move = sum(arr2[:arr2_pointer])
      
#         # arr1_sum = arr1_total-arr1_move + arr2_move
#         # arr2_sum = arr2_total-arr2_move + arr1_move 

#         # queue 가 추가 될 수 도 있음   

#         if arr1_sum == arr2_sum:
#             print('df')
#             count = min(count, arr1_pointer + arr2_pointer)
#             arr1_pointer += 1
#             arr2_pointer = 0
#             if arr1_pointer < N and arr2_pointer < N:
#               arr1_sum -= arr1[arr1_pointer-1]
#               arr2_sum = arr2_total + (arr1_total - arr1_sum)
#             else:
#               break
#             # 이동            

#         elif arr1_sum < arr2_sum:
#             arr2_pointer += 1
#             if arr2_pointer < N:
#               arr1_sum += arr2[arr2_pointer-1]
#               arr2_sum -= arr2[arr2_pointer-1]
#             else:
#                 break
          
#         elif arr1_sum > arr2_sum:
#             arr1_pointer += 1
#             arr2_pointer = 0
#             if arr1_pointer < N and arr2_pointer < N:
#               arr1_sum -= arr1[arr1_pointer-1]
#               arr2_sum = arr2_total + (arr1_total - arr1_sum)
#             else:
#               break
    
#     return count

def twoPointer(arr,N,M):
  left,right = 0,1

  count = 1e9
  print(arr,N,M)  
  while right <= N and left <= right:

    arr_sums = arr[left:right]
    total = sum(arr_sums)

    if total == M:
      
      halfN = N//2
      if left < halfN:
        tmp = left + right - halfN        
      else:
        if left == halfN:
          tmp = halfN + (right-left)
        elif right==N and left ==N-1:
          tmp = right-halfN
        else:          
          # 특이 케이스
          tmp = (right-halfN)+halfN+(left-halfN)
      count = min(tmp, count)
      right += 1
      
    elif total > M:
      left +=1
    elif total < M:
      right +=1

  return count


def solution(queue1, queue2):

    total = sum(queue1) + sum(queue2)    
    if total % 2 != 0: # 만들 수 없는 경우
      return -1
    m = total // 2
    arr = queue1 + queue2
    n = len(arr)
    answer = twoPointer(arr,n,m)
    
    return answer


q1 = [3, 2, 7, 2]
q2 = [4, 6, 5, 1]

q1 = [1, 2, 1, 2]
q2 = [1, 10, 1, 2]

# q1 = [1,1]
# q2 = [1,5]

a = solution(q1,q2)
print(a)