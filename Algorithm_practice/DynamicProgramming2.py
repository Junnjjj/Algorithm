#1로 만들기

#x 입력받기
x = int(input())

#연산횟수 
d = [0] * 30001

for i in range(3, x+1):
  #1로 빼는 경우  
  d[i] = d[i-1] + 1

  if i%2 == 0:
    d[i] = min(d[i], d[i//2] +1)
  if i%3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  if i%5 == 0:
    d[i] == min(d[i], d[i//5] + 1)

print(d[x])