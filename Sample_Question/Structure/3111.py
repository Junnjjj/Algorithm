import sys
input = sys.stdin.readline

def solution(a,t):
  a_size = len(a)
  t_size = len(t)

  left_stack = []
  right_stack = []

  left = 0
  right = t_size - 1

  checkSide = True
  while left <= right:

    if checkSide: # 왼쪽에서 접근
      left_stack.append(t[left])
      left += 1

      if left_stack[-1] == a[-1]:
        
        if ''.join(left_stack[-1*a_size:]) == a:
          del left_stack[-1*a_size:]
          checkSide = False # 오른쪽으로 넘어감
      
    else: # 오른쪽에서 접근
      right_stack.append(t[right])
      right -= 1

      if right_stack[-1] == a[0]:

        if ''.join(right_stack[-1*a_size:]) == a[::-1]:
          del right_stack[-1*a_size:]
          checkSide = True

  result = []
 
  if checkSide: # 왼쪽에서 끝나면
    # 오른쪽으로 더해줘서 오른쪽에서 찾아줘야함
    left_stack.reverse()
    temp = len(right_stack)
    t = right_stack + left_stack
    for i in range(len(t)):      
      
      if i > temp:
        break
      
      if t[i] == a[-1]:

        if ''.join(t[-1*a_size:]) == a[::-1]:
          del t[i:a_size] 
          break

    t.reverse()
    
  else: # 오른쪽에서 끝나면
    # 오른쪽스택을 reverse 
    right_stack.reverse()
    temp = len(left_stack)
    t = left_stack + right_stack
    for i in range(len(t)):
      
      if i >= temp:
        break

      if t[i] == a[0]:        
        if ''.join(t[i:a_size]) == a:
          del t[i:a_size]
          break

  return ''.join(t)  
    
A = str(input().rstrip())
T = str(input().rstrip())

ans = solution(A,T)
print(ans)



# 1 T에 A가 없으면 알고리즘을 종료한다.
# 2 T에서 처음 등장하는 A를 찾은 뒤, 삭제한다.
# 3 T에 A가 없으면 알고리즘을 종료한다.
# 4 T에서 마지막으로 등장하는 A를 찾은 뒤, 삭제한다.
# 5 1번으로 돌아간다.

# 처음 마지막

# print(A, T)
