#효율적인 화폐구성

#n 종류의 화폐, M 화폐의 가치
n, m = map(int, input().split())

array = []
for i in range(n):
  array.append(int(input()))

#M을 array로 만들 수 있는 최소 개수

d = [0] * 100

#array 에 있는 동전 수 횟수에 더하기
for i in array:
  d[i] = 1


for i in range(max(array)+1, m+1):
  for j in array:
    if d[i-j] > 0:
      result = m
      result = min(result, d[i-j])
      d[i] = result + 1

