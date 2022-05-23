# import sys
# from collections import deque

# input = sys.stdin.readline

# def strList(arr):
#   string_list = []
#   for i in range(len(arr[0])):
#     temp = ''
#     for j in range(len(arr)):
#       temp += arr[j][i]
#     string_list.append(temp)
#   return string_list
    

# r,c = map(int,input().split())

# strings = deque()
# for _ in range(r):
#   word = str(input().rstrip())
#   strings.append(word)

# answer = -1
# while True:  
#   temp = strList(strings)
#   if len(list(set(temp))) != len(temp):
#     print(answer)
#     break
#   strings.popleft()
#   if len(strings) == 0:
#     print(answer+1)
#     break
  
#   answer +=1

# from collections import defaultdict
# R,C = map(int,input().split())
# arr = [list(input()) for _ in range(R)]

# result = 0
# start, end = 0, R-1
# while start <= end:
#     mid = (start+end)//2

#     # 문자열 중복 확인
#     isOK = True
#     dict = defaultdict(int)
#     print(dict)
#     for j in range(C):
#         temp = ''
#         for i in range(mid, R):
#             temp += str(arr[i][j])
#         if not dict[temp]:
#             dict[temp] += 1
#         else:
#             isOK = False
#             break

#     if isOK:
#         result = mid
#         start = mid + 1
#     else:
#         end = mid - 1

# print(result)

# 세로로 문자열들을 모두 뽑아온다음에 reverse후 정렬한다음 인접한 것끼리 몇개가 겹치는지 최대값을 찾아주면 된다.

import sys

input = sys.stdin.readline

r,c = map(int,input().split())
strings = [list(str(input().rstrip())) for _ in range(r)]

new_strings = []
for j in range(c):
  temp = ''
  for i in range(r-1,-1,-1):
    temp += strings[i][j]
  new_strings.append(temp)

answer = 0
for i in range(c):
  a = new_strings[i]
  for j in range(i,c):
    if i == j: continue
    count = 0
    b = new_strings[j]
        
    for idx in range(r):
      if a[idx] != b[idx]:
        break
      count += 1

    answer = max(answer, count)

    
print(r-1 if answer == 0 else r-(answer + 1))

# 4 6
# mrvica
# mrvica
# marica
# mateja

# 3 4
# alfa
# zeta
# beta

# # 2
# 3 4
# beta
# zeta
# alfa

