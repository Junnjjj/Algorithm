# Greedy
import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int,input().split()))

items.sort()

answer = 1
for num in items:
  if answer < num:
    break

  answer += num

print(answer)
    
  