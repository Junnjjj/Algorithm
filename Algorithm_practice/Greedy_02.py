n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/k)
index = m%k

result = count*(first*k + second) + first*index

print(result)