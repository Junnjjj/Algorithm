#모험가 길드

#n 입력
n = int(input())

#공포도 x 이상인 모험가는 X명 이상으로 구성한 모험가 그룹에 참여해야함

data = []
#공포도 입력
data = list(map(int, input().split()))
data.sort( reverse= True)

group = [0] * (n + 1) 


start = data[0]
# group[start] += 1
result = 1

for i in range(len(data)):
  if start == i+1:
    result +=1
    start = data[i]

print(result)