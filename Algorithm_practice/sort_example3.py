#위에서 아래로

#N을 입력 받기
n = int(input())

#n 개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

array.sort(reverse = True)

print(array)

#성적이 낮은 순서로 학생 출력하기
n = int(input())

array = []
for i in range(n):
  array.append(input().split())

array.sort(key = lambda x : x[1])

print(array)

#두 배열의 원소 교체
n, k = map(int, input().split())

#input array A, B
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] <= b[i]:
    a[i] = b[i]

print(sum(a))


  