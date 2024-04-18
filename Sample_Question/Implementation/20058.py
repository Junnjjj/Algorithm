# 20058

import sys
from collections import deque
input = sys.stdin.readline

n,q = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(2**n)]
lArr = list(map(int,input().split()))


def rotate_90_degrees(matrix):
	n = len(matrix)
	rotated_matrix = [[0] * n for _ in range(n)]

	for i in range(n):
			for j in range(n):
					rotated_matrix[j][n-1-i] = matrix[i][j]

	return rotated_matrix

def rotate_data(board,l):	
	temp_board = [[0]*2**n for _ in range(2**n)]

	size = 2**n//2**l  # 총 격자 칸	
	for i in range(size):
		xIdx = i*(2**l)
		for j in range(size):
			yIdx = j*(2**l)			

			temp = [[0]*(2**l) for _ in range(2**l)]
			for k in range(2**l): 
				dx = xIdx+k
				for m in range(2**l):
					dy = yIdx+m					

					temp[k][m] = board[dx][dy]	

			rotate_temp = rotate_90_degrees(temp)			
			for k in range(2**l):
				dx = xIdx+k
				for m in range(2**l):
					dy = yIdx+m
					temp_board[dx][dy] = rotate_temp[k][m]

	return temp_board

def meltingIce(board):
	move = [(1,0),(-1,0),(0,1),(0,-1)]	
	minusBoard = [[0]*len(board) for _ in range(len(board))]

	for i in range(len(board)):
		for j in range(len(board)):

			minus_check = 0
			if board[i][j] == 0: continue # 얼음이 아닐경우 넘어감			
			for nx,ny in move:								

				dx,dy = i+nx,j+ny
				if dx < 0 or dx >= len(board) or dy < 0 or dy >= len(board):										
					continue				
				if board[dx][dy] > 0:					
					# 얼음이 주변에 있는경우
					minus_check += 1

			if minus_check >= 3: continue # 주변에 얼음이 3개 이상일 경우 넘어가고							
			else: 
				# print(i,j,minus_check)
				minusBoard[i][j] -= 1 # 아니면, 해당 부분은 -1


	for i in range(len(board)):
		for j in range(len(board)):
			if minusBoard[i][j] == 0: continue			
			board[i][j] += minusBoard[i][j]

	return board

def bigIce(board):
	move = [(1,0),(-1,0),(0,1),(0,-1)]	
	visited = [[False]*len(board) for _ in range(len(board))]
	result = 0

	q = deque()
	for i in range(len(board)):
		for j in range(len(board)):
			ice_sum = 0
			if not visited[i][j] and board[i][j] > 0:
				q.append((i,j))
				ice_sum += 1
				visited[i][j] = True

				while q:
					x,y = q.popleft()
					for nx,ny in move:
						dx,dy = x+nx,y+ny
						if dx < 0 or dx >= len(board) or dy < 0 or dy >= len(board) or board[dx][dy] == 0 or visited[dx][dy]:
							continue
						q.append((dx,dy))
						ice_sum += 1
						visited[dx][dy] = True

				result = max(result, ice_sum)

	return result


def solution(data):

	for l in lArr:
		board = rotate_data(data,l)			
		board = meltingIce(board)		
		data = board

	ans1,ans2 = 0,0
	for row in board:				
		ans1 += sum(row)
	ans2 = bigIce(board)

	print(ans1)
	print(ans2)



solution(data)

	# 첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 
	# 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다.