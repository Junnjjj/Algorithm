#정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지
#3이 하나라도 포함되는 모든 경우의 수 작성

#N 입력
n = int(input())

count = 0
for i in range(n+1): #hour
  for j in range(60): #min
    for k in range(60): #sec
      if '3' in str(i) + str(j) + str(k):
        count += 1
      

print(count)

