import sys
input = sys.stdin.readline

minsik = 'a b k d e g h i l m n ng o p r s t u w y'
minsik = minsik.split(' ')
minsik_dict = {k:v for v,k in enumerate(minsik)}

def solution(word_lst):  

  change_to_num = []
  for idx,word in enumerate(word_lst):
    check = False
    temp = []
    for i,letter in enumerate(word):
      if letter != 'n':
        temp.append(minsik_dict[letter])
      else:
        if i == len(word) or word[i:i+2] != 'ng':
          temp.append(minsik_dict[letter])
        else:
          temp.append(minsik_dict['ng'])
          check = True
      if check:
        check = False
        continue

    change_to_num.append((temp,idx))
  
  change_to_num.sort(key = lambda x: x[0])
  for item,i in change_to_num:
    print(word_lst[i])

        
strings = []
n = int(input())
maxLen = 0
for _ in range(n):
  string = str(input().rstrip())  
  strings.append(string)

solution(strings, maxLen)