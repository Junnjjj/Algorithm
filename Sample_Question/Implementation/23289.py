# implemation :  23289 온풍기 안녕
import sys
from collections import deque
input = sys.stdin.readline

r,c,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(r)]
w = int(input())
walls = []
wall_dict = {}
for _ in range(w):
	x,y,t = map(int,input().split())
	x -= 1
	y -= 1
	walls.append((x,y,t))
	if t == 0:
		wall_dict[(x,y)] = [2] if not (x,y) in wall_dict else wall_dict[(x,y)] + [2]
		wall_dict[(x-1,y)] = [3] if not (x-1,y) in wall_dict else wall_dict[(x-1,y)] + [3]
	else:
		wall_dict[(x,y)] = [0] if not (x,y) in wall_dict else wall_dict[(x,y)] + [0]
		wall_dict[(x,y+1)] = [1] if not (x,y+1) in wall_dict else wall_dict[(x,y+1)] + [1]

# t = 0 일 때(x, y)와 (x-1, y) 사이 벽
# t = 1 일 때(x, y)와 (x, y+1) 사이 벽

# 조사하는 모든 칸의(5) 온도가 K 이상이 되었는지 확인 => 안되어있으면 반복
# 이 떄 반복횟수 구하기,

# 1, 2, 3, 4 => 오른쪽, 왼쪽, 위, 아래
move = [(0,1),(0,-1),(-1,0),(1,0)] # 오른쪽, 왼쪽, 위, 아래
board = [[0]*c for _ in range(r)]
heater = []
search_k = []
for i in range(r):
	for j in range(c):
		if 0 < data[i][j] < 5:
			heater.append((i,j,data[i][j]))
		elif data[i][j]:
			search_k.append((i,j))

def heater_s(board, heater):
	q = deque()
	for x,y,dir in heater:
		dir -= 1
		oppsite = dir - 1 if dir % 2 == 1 else dir + 1
		temperature = 5

		dx,dy = x+move[dir][0], y+move[dir][1]
		if dx < 0 or dx >= r or dy < 0 or dy >= c: continue
		board[dx][dy] += temperature
		visited = []
		q.append((dx,dy,temperature))

		# 왼쪽, 오른쪽으로 퍼짐
		if dir == 2 or dir == 3:
			spread_dir_left = move[1]
			spread_dir_right = move[0]
			left = 1
			right = 0
		# 위, 아래로 퍼짐
		else:
			spread_dir_left = move[2]
			spread_dir_right = move[3]
			left = 2
			right = 3 		

		while q:
			prevX,prevY,temp = q.popleft()
			if temp == 1: continue
			# 3방향으로 퍼짐

			nextX1,nextY1 = prevX+move[dir][0], prevY+move[dir][1]
			nextX2,nextY2 = nextX1+spread_dir_left[0], nextY1+spread_dir_left[1]
			nextX3,nextY3 = nextX1+spread_dir_right[0], nextY1+spread_dir_right[1]
			# visited 도 추가해줘야함 , ㅅㅂ

			check = True
			if 0 <= nextX1 < r and 0 <= nextY1 < c and not (nextX1,nextY1) in visited:
				if (prevX,prevY) in wall_dict and dir in wall_dict[(prevX,prevY)]:
					check = False
				if check:
					q.append((nextX1,nextY1,temp-1))
					visited.append((nextX1,nextY1))
					board[nextX1][nextY1] += temp-1

			check = True
			if 0 <= nextX2 < r and 0 <= nextY2 < c and not (nextX2,nextY2) in visited:
				if (prevX,prevY) in wall_dict and left in wall_dict[(prevX,prevY)]:
					check = False
				if (nextX2,nextY2) in wall_dict and oppsite in wall_dict[(nextX2,nextY2)]:
					check = False
				if check:
					q.append((nextX2,nextY2,temp-1))
					visited.append((nextX2,nextY2))
					board[nextX2][nextY2] += temp-1

			check = True
			if 0 <= nextX3 < r and 0 <= nextY3 < c and not (nextX3,nextY3) in visited:
				if (prevX,prevY) in wall_dict and right in wall_dict[(prevX,prevY)]:
					check = False
				if (nextX3,nextY3) in wall_dict and oppsite in wall_dict[(nextX3,nextY3)]:
					check = False
				if check:
					q.append((nextX3,nextY3,temp-1))
					visited.append((nextX3,nextY3))
					board[nextX3][nextY3] += temp-1

	return board

def spread_area(board):
	tempBoard = [[0]*c for _ in range(r)]	
	for i in range(r):
		for j in range(c):
			x,y = i,j
			for d in range(4):
				dx,dy = x+move[d][0],y+move[d][1]
				if dx < 0 or dx >= r or dy < 0 or dy >= c: continue
				if board[x][y] <= board[dx][dy]: continue				

				# 벽 조건추가
				if (x,y) in wall_dict and d in wall_dict[(x,y)]: continue

				temp = (board[x][y] - board[dx][dy]) // 4				
				tempBoard[x][y] -= temp
				tempBoard[dx][dy] += temp

	for i in range(r):
		for j in range(c):
			board[i][j] += tempBoard[i][j]

	return board

def minus_boundary(board):
	for i in range(r):
		for j in range(c):
			if i == 0 or i == r - 1 or j == 0 or j == c - 1:
				if board[i][j] > 0:
					board[i][j] -= 1

	return board


def check_k(board):
	result = 0
	for x,y in search_k:
		if board[x][y] < k:
			return False
	return True


def solution():
	chocholte = 0

	while True:
		if chocholte > 100:
			print(101)
			break

		newBoard = heater_s(board, heater)
		newBoard = spread_area(newBoard)
		newBoard = minus_boundary(newBoard)
		chocholte += 1
		if check_k(newBoard): 
			print(chocholte)
			break

solution()
