# 20057

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
# 왼쪽 아래 오른쪽 위
move = [(0,-1), (1,0), (0,1), (-1,0)]

def spread_sand(r,c,dir):
	global answer
	nowSand = data[r][c]
	if nowSand == 0: return

	go = move[dir]
	opposite = move[dir + 2] if dir <= 1 else move[dir - 2]
	up = 3 if dir == 0 or dir == 2 else 2 # 위, 오른쪽 
	down = 1 if dir == 0 or dir == 2 else 0 # 아래, 왼쪽

	temp = 0
	# 범위 밖으로 나가면 global answer += 모래양
	# dir dir 5%
	x,y = r+go[0]*2, c+go[1]*2
	sand = int(nowSand * 0.05)
	if sand > 0:
		temp += sand
		if x < 0 or x >= n or y < 0 or y >= n:
			answer += sand
		else:
			data[x][y] += sand

	for dx,dy in (move[up],move[down]):
		# 위 dir : 10%
		x,y = r+dx+go[0], c+dy+go[1]
		sand = int(nowSand * 0.1)
		if sand > 0: 
			temp += sand
			if x < 0 or x >= n or y < 0 or y >= n: # 범위 밖 나가면 ..
				answer += sand
			else: # 모래양 더함
				data[x][y] += sand
		else: continue # 0보다 작으면 밑에도 다 0보다 작음 볼필요도 없음

		# 바로 위 : 7 %
		x,y = r+dx, c+dy	
		sand = int(nowSand * 0.07)
		if sand > 0: 
			temp += sand
			if x < 0 or x >= n or y < 0 or y >= n: # 범위 밖 나가면 ..
				answer += sand
			else: # 모래양 더함
				data[x][y] += sand
		else: continue

		# 위 위 : 2 %
		x,y = r+(2*dx), c+(2*dy)
		sand = int(nowSand * 0.02)
		if sand > 0: 
			temp += sand
			if x < 0 or x >= n or y < 0 or y >= n: # 범위 밖 나가면 ..
				answer += sand
			else: # 모래양 더함
				data[x][y] += sand

		# 위 opposite : 1%
		x,y = r+dx+opposite[0], c+dy+opposite[1]
		sand = int(nowSand * 0.01)
		if sand > 0: 
			temp += sand
			if x < 0 or x >= n or y < 0 or y >= n: # 범위 밖 나가면 ..
				answer += sand
			else: # 모래양 더함
				data[x][y] += sand

	aSand = nowSand - temp # a 로 갈 샌드양
	x,y = r+go[0], c+go[1]
	if x < 0 or x >= n or y < 0 or y >= n:
		answer += aSand
	else:
		data[x][y] += aSand

def tornado():
	# 중앙에서부터 빙빙 돌아서 0,0 까지 도착
	# 왼쪽, 아래, 오른쪽, 위	
	# 2 부터 ~ N 까지 2번씩 증가
	mid = (n//2)
	lenght = 2
	dir = 0 # 0,1  일 때는 length 2 , 2,3 일떄는 
	dx,dy = mid,mid

	temp = 1
	cnt = 0
	global answer
	while True:
		# print(dx,dy) # 이전칸 출력

		spread_sand(dx,dy,dir)
		if dx == 0 and dy == 0: break

		if temp == lenght:
			dir = (dir + 1) % 4
			temp = 1
			if dir == 2 or dir == 0:
				lenght += 1

		nx,ny = move[dir][0], move[dir][1]
		dx,dy = dx+nx, dy+ny # 한칸 이동
		temp += 1			



def solution():
	global answer
	answer = 0
	# 격자 밖으로 나간 모래 양 구하기
	tornado()

	print(answer)
	return

solution()