import sys

input = sys.stdin.readline

string = input().rstrip()
p = "PPAP"
stack = []

for char in string:
  stack.append(char)
  if "".join(stack[-4:]) == p:
    del stack[-4:]    
    stack.append("P")

if "".join(stack) != 'P':
  print("NP")
else:
  print("PPAP")
