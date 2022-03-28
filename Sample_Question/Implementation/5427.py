import sys
from collections deque
input =sys.stind.readline


def fire(r,c):
  


n = input().rstrip()
for _ in range(n):
  w,h =map(int,input().split())
  graph = []
  fire = []
  location = []
  for i in range(w):
    data = list(input().rstrip())
    for j in range(h):
      if data[j] == '*':# 불일경우
        fire.append((i,j))
      elif data[j] == '@': # 상근일 경우
        location.append((i,j))


while True:
  fire()