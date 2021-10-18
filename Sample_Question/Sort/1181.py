import sys

n = int(input())

data = [sys.stdin.readline().rstrip() for _ in range(n)]

data.sort()
print(data)