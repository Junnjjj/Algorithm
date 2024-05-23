# 21610 : implementation

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dirs = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

# 비바라기 .
def rain_hope(clouds, di,si):
	# (N, 1), (N, 2), (N-1, 1), (N-1, 2) 에 구름이 생김
	rain_area = []

	# 1. 모든 구름이 di 방향으로 si 만큼 이동
	for x,y in clouds:

		dx = x + dirs[di][0]*si
		dy = y + dirs[di][1]*si

		if dx >= 0:
			dx = dx % n
		else:
			while dx < 0:
				dx += n 

		if dy >= 0:
			dy = dy % n
		else:
			while dy < 0:
				dy += n


		# 5,6,7,8,9 => 0,1,2,3,4 => % n
		# -5,-4,-3,-2,-1 => 0,1,2,3,4

	# 2. 구름이 있는 칸에 +1 만큼 증가
		data[dx][dy] += 1
		rain_area.append((dx,dy))

	# 3. 구름이 사라짐

	# 4. 2에서 증가한 칸에 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
	for area in rain_area:
		basket = 0

		x,y = area
		for i,dir in enumerate(dirs):
			if i % 2 == 0 and i > 0:
				dx,dy = dir

				nx,ny = x+dx,y+dy

				if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > 0:
					basket += 1

		data[x][y] += basket			


	# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
	newClouds = []
	for i in range(n):
		for j in range(n):
			if data[i][j] >= 2 and (i,j) not in rain_area:
				newClouds.append((i,j))
				data[i][j] -= 2


	return newClouds

def solution():
	clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]	

	for move in moves:
		di,si = move
		clouds = rain_hope(clouds, di, si)

	answer = 0
	for row in data:
		answer += sum(row)

	print(answer)


solution()