# 17779
import sys
from collections import deque
from itertools import product
input = sys.stdin.readline


n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

Bmove = [(1,-1),(1,1)]
data_sum = 0
for row in data:
	data_sum += sum(row)

def outOfBoundary(x,y,d1,d2):	
	if x+d1 < 0	or x+d1 >= n or y-d1 < 0 or y-d1 >= n: return False
	if x+d2 < 0	or x+d2 >= n or y+d2 < 0 or y+d2 >= n: return False
	if x+d1+d2 < 0 or x+d1+d2 >= n or y-d1+d2 < 0 or y-d1+d2 >= n: return False
	return True

def bfs(x,y,d1,d2):
	# 인구가 가장 큰 선거구 - 인구가 가장 큰 선거구 return	
	board = [[False] * n for _ in range(n)]
	board[x][y] = True
	dx,dy = x,y
	for i in range(d1+d2):
		idx = 0 if i < d1 else 1
		dx,dy = dx+Bmove[idx][0], dy+Bmove[idx][1]
		board[dx][dy] = True
	dx,dy = x,y
	for i in range(d2+d1):
		idx = 1 if i < d2 else 0
		dx,dy = dx+Bmove[idx][0], dy+Bmove[idx][1]
		board[dx][dy] = True


	a1,a2,a3,a4,a5 = 0,0,0,0,0
	# 1 구역
	for i in range(x+d1):
		for j in range(y+1):
			if board[i][j]: break
			a1 += data[i][j]
	for i in range(x+d2+1):
		for j in range(n-1, y, -1):
			if board[i][j]: break
			a2 += data[i][j]
	for i in range(x+d1,n):
		for j in range(y-d1+d2):
			if board[i][j]: break
			a3 += data[i][j]
	for i in range(x+d2+1,n):
		for j in range(n-1,y-d1+d2-1, -1):
			if board[i][j]: break
			a4 += data[i][j]


	a5 = data_sum - (a1+a2+a3+a4)
	return max(a1,a2,a3,a4,a5) - min(a1,a2,a3,a4,a5)

def solution():
	ans = 1e9
	d_arr = [i for i in range(1,n)]
	d_possible = list(product(d_arr,repeat = 2))	

	for x in range(n):
		for y in range(n):
			for d1,d2 in d_possible:
				if not outOfBoundary(x,y,d1,d2): continue # 범위 벗어나면 							
				ans = min(ans, bfs(x,y,d1,d2))

	print(ans)

solution()
