import sys

input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.

ans = False
while B:
  if B[-1] == 'A':
    B.pop()
  elif B[-1] == 'B':
    B.pop()
    B.reverse()

  if A == B:
    ans = True
    break

print(1 if ans else 0)