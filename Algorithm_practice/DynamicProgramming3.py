#개미 전사

#첫째 줄에 식량창고의 개수 N
n = int(input())

#둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다.
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

#바닥 공사

#첫째 줄에 N이 주어진다
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
  d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])