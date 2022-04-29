import sys

input = sys.stdin.readline

# n = int(input())
# array = list(map(int,input().split()))


# # 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 값 
# # 10 -4 3 1 5 6 -35 12 21 -1

# dp = [0] * (n+1)

# for i in range(n):
#   temp = array[i]
#   for j in range(i,n):
#     if temp < sum(array[i:j]):
#       dp[i] = sum(array[i:j])
#       temp = dp[i]

# print(max(dp))


n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]

for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))

