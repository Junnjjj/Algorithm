import sys
from collections import deque
input = sys.stdin.readline

# ()(((()())(())()))(())

data = list(map(str,input().rstrip()))
size = len(data)

laser = []
stick = []
for i in range(size-1):
	if data[i] == '(' and data[i+1] == ')':
		laser.append(i) # laser 시작 좌표를 배열에 삽입		

q = deque()
for i in range(size):
	if i in laser or i-1 in laser: continue # laser 이면 넘어감

	if data[i] == '(':
		q.append(i)

	elif data[i] == ')':
		leftPoint = q.pop()
		rightPoint = i	
		stick.append((leftPoint, rightPoint))

answer = 0
for left,right in stick:
	temp = 0
	for l in laser:
		if left < l < right:
			temp += 1

	answer += (temp + 1)

print(answer)
