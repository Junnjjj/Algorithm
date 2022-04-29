import sys

input = sys.stdin.readline

n = int(input())

rgb = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(3):
    idx = []
    for k in range(3):
      if k == j:
        continue
      idx.append(k)

    rgb[i][j] = rgb[i][j] + min(rgb[i-1][idx[0]], rgb[i-1][idx[1]])

print(min(rgb[n-1))


# n = int(input())
# p = []
# for i in range(n):
#     p.append(list(map(int, input().split())))
# for i in range(1, len(p)):
#     p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
# print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))

# 3
# 26 40 83
# 49 60 57
# 13 89 99