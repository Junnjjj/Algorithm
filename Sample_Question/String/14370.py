import sys

input = sys.stdin.readline

alpha_dict = {1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE", 0:"ZERO"}

def appendItem(answer,string,num):
  answer.append(num)
  for item in alpha_dict[num]:
    string.remove(item)

def solution(string,i):

  answer = []
  string = list(string)
    
  while True:    
    temp = len(string)
    if 'Z' in string:
      appendItem(answer,string,0)    
    if 'X' in string:
      appendItem(answer,string,6)    
    if 'U' in string:
      appendItem(answer,string,4)    
    if 'G' in string:
      appendItem(answer,string,8)    
    if 'W' in string:
      appendItem(answer,string,2) 

    if temp == len(string):
      break
    
  while True:
    temp = len(string)
    if 'F' in string:
      appendItem(answer,string,5)    
    if 'O' in string:
      appendItem(answer,string,1)    
    if 'R' in string:
      appendItem(answer,string,3)  

    if temp == len(string):
      break

  while True:
    temp = len(string)
    if 'V' in string:
      appendItem(answer,string,7)    

    if temp == len(string):
      break

  while True:
    temp = len(string)
    if "I" in string:
      appendItem(answer,string,9)    

    if temp == len(string):
      break

  answer.sort()  
  answer = list(map(lambda x: str(x), answer))

  return "Case #%d: %s" %(i+1, str(''.join(answer))) 
  

ans = []
n = int(input())
for i in range(n):
  word = str(input().rstrip())

  a = solution(word,i)
  ans.append(a)

for item in ans:
  print(item)