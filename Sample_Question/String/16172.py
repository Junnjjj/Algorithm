import sys

input = sys.stdin.readline

def kmp(s,p):
  global table

  j = 0
  for i in range(len(s)):    
    while j >0 and s[i] != p[j]:
      j = table[j-1]

    if s[i] == p[j]:
      if j == len(p)-1:         
        print(1)
        exit()
        j = table[j]
      else:
        j+= 1

def make_table(p):
  global table

  j =0
  for i in range(1, len(p)):  
    while j > 0 and p[i] != p[j]:
      j = table[j-1]

    if p[i] == p[j]:
      j += 1
      table[i] = j

string = input().rstrip()
newstring = ''.join([i for i in string if not i.isdigit()])
pattern = input().rstrip()

table = [0] * len(pattern)
make_table(pattern)

kmp(newstring,pattern)
print(0)