import sys
import string

input = sys.stdin.readline

alpha_dict = {k:v for v,k in enumerate(string.ascii_uppercase)}

def solution(string):

  answer = 0
  for i in string:
    num = alpha_dict[i] if alpha_dict[i] <= 12 else 26 - alpha_dict[i]    
    answer += num  

  length = len(string)
  min_move = length - 1
  for i in range(length):
      next_i = i + 1  # 현재 알파벳 이후로 처음 만나는 A가 아닌 알파벳의 인덱스
      while next_i < length and string[next_i] == 'A':
          next_i += 1
    
      min_move = min(min_move, i + (i + length - next_i), 2 * (length - next_i) + i)

  answer += min_move
  print(answer)
  
  
n = int(input())

for _ in range(n):
  name = str(input().rstrip())
  solution(name)




# 가장 처음에 화면에 나와있는 이름은 'A'로만 이루어져 있다. 또, 이름의 첫 글자가 선택되어 있다. 조이스틱을 앞으로 움직이면 선택된 글자가 알파벳 다음 글자로 바뀐다. 조이스틱을 뒤로 움직이면, 알파벳 이전 글자로 바뀐다. 'Z'의 다음 글자는 'A'이고, 'A'의 이전 글자는 'Z'이다.

# 조이스틱을 왼쪽으로 움직이면, 현재 선택한 글자의 왼쪽 글자를 선택하게 되고, 오른쪽으로 움직이면 오른쪽 글자를 선택하게 된다. 가장 왼쪽 글자가 선택되었을 때, 조이스틱을 왼쪽으로 움직이면 마지막 글자를 선택하게 되고, 마지막 글자를 선택했을 때, 오른쪽으로 움직이면 첫 글자를 선택하게 된다.

# 2
# JEROEN
# JAN



# 이름의 최대 길이 1000
# AAAAAA
# JEROEN
# 9 4 17 14 4 13 
# 9 4 9 12 4 13 => 최소값

  # 9 13          22
               
  
# print(alpha_dict)

# for i in 'JEROEN':
#   num = alpha_dict[i]
#   if num > 13:
#     num = 25 - num + 1
#   print(num, end= ' ')

# AAAAABAAABA