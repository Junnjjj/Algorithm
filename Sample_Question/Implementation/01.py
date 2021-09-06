n = input()

length = len(n)


left = 0
for i in range(length // 2):
  left += int(n[i])

right = 0
for j in range(length //2 , length):
  right += int(n[i])

if left == right:
  print("LUCKY")
else:
  print("READY")