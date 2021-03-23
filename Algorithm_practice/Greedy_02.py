n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#f k개, s 1개  m / k+1
count = int(m/(k+1))
index = m%(k+1)

result = count*(first*k + second) + first*index

print(result)