import sys

input = sys.stdin.readline

# s = str(input().rstrip())
# t = str(input().rstrip())

# while True:
#   s_size = len(s)
#   s = s.replace(t,'')
#   if s_size == len(s):
#     break
# print(s)


string = str(input().rstrip())    # 전체 문자열
bomb = str(input().rstrip())      # 폭발 문자열

lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
stack = []
length = len(bomb)  # 폭발 문자열의 길이

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)
print(answer)