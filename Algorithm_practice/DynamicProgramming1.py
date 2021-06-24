#Dynamic programming

#큰 문제를 작은 문제로 나눌 수 있다
#작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서 동일하다.

# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   return fibo(x-1) + fibo(x-2)

# print(fibo(4))

d = [0] * 100 # 메모제이션을 위한 리스트 초기화

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
  #종료 조건
  if x == 1 or x == 2:
    return 1
  #이미 계산된 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))

#피보나치수열 (바텀 업 다이나믹 프로그래밍)
d = [0] * 100

#첫번째 피보나치수열
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])