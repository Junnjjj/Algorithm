# n x m 행렬
n, m = map(int, input().split())

result = 0
#행렬 입력
for _ in range(n):
  data = list(map(int, input().split()))

  min_value = min(data)

  result = max(result, min_value)

print(result)

