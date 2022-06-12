import sys
input = sys.stdin.readline

string = str(input().rstrip())

answer = 0
temp = ''
check = False
last = ''
for i in string:
  if i != '+' and i != '-':    
    temp += i
  elif i == '+':
    answer += int(temp)    
    temp = ''
    last = '+'
  elif i == '-' and not check:
    # 다음 '-' 나올 때 까지 괄호
    check = True
    answer += int(temp)    
    temp = ''
    last = '-'
  elif i == '-' and check:
    # - 를 만나면
    check = False
    answer -= int(temp)    
    temp = ''
    last = '-'

if last == '+':
  answer += int(temp)
else:
  answer -= int(temp)
print(answer)
    

# 10+20+30+40
# 10+20-30+40
# 10+20-30+40-100

# 마이너스 부터 마이너스까지 () 채움