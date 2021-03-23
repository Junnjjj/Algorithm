#N이 1 이 될 때 까지 두 과정 반복하여 수행 , K로 나누는 연산은 나누어 떨어질때만 수행
#N에서 1을 뺀다
#N을 K로 나눈다

#n, k 입력
n, k = map(int, input().split())

count = 0

while n != 1:
  # n이 k로 나누어 떨어지면
  if n%k == 0:
    n = n / k
    count += 1
    continue
  n -= 1
  count +1

print(count)