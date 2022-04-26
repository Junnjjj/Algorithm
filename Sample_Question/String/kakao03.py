def findCollectString(s):    
    size = len(s)
    while True:
        s = s.replace('()','')
        if size == len(s):
            break
        size = len(s)
    return True if len(s) == 0 else False

a = '(()())'
a = '((()())())'

# findCollectString(a)
c = a[1:-1]
print(a[1:-1])
newA = ''
for item in c:
  newA += ')' if item == '(' else '('
print(newA)