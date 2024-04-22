# 20056

import sys
from collections import deque
input = sys.stdin.readline


n,m,k = map(int,input().split())
fireBalls = [list(map(int,input().split())) for _ in range(m)] # m 개의 Fireball, r,c,m,s,d

move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def moveFireBall(board):
	temp_board = []
	for _ in range(n):
		temp = []
		for _ in range(n):
			q = deque()
			temp.append(q)
		temp_board.append(temp)


	for i in range(n):
		for j in range(n):
			if not board[i][j]: continue # 비어 있으면 지나감

			q = deque()
			while board[i][j]:
				mi,si,di = board[i][j].popleft()
				# d 방향으로 s 칸 만큼 이동 
				dx,dy = i,j				
				dx,dy = i+move[di][0]*si, j+move[di][1]*si
				if dx >= n:
					dx = dx%n
				elif dx < 0:
					while dx < 0:
						dx = n + dx

				if dy >= n:
					dy = dy%n
				elif dy < 0:
					while dy < 0:
						dy = n + dy

				temp_board[dx][dy].append((mi,si,di))

	return temp_board


def concatFireBall(board):
	for i in range(n):
		for j in range(n):
			# firebase 이 합쳐짐
			if board[i][j] and len(board[i][j]) >= 2: 

				m_sum = 0 # 무게 총합
				s_sum = 0 # 속력의 합
				f_sum = len(board[i][j]) # 파이어볼의 수				
				di_arr = []
				while board[i][j]:
					mi,si,di = board[i][j].popleft()

					m_sum += mi
					s_sum += si

					# 방향이 모두 홀수이거나, 모두 짝수이면 0,2,4,6 그렇지 않으면 1,3,5,7
					di_arr.append(di%2)

				if 0 in di_arr and 1 in di_arr:					
					di_arr = [1,3,5,7]					
				else:
					di_arr = [0,2,4,6]

				new_mi = m_sum // 5
				if new_mi == 0: continue
				new_si = s_sum // f_sum
				for new_di in di_arr:
					board[i][j].append((new_mi,new_si,new_di))

def calMi(board):
	result = 0
	for i in range(n):
		for j in range(n):
			if board[i][j]:
				for mi,si,di in board[i][j]:
					result += mi
	return result

def solution():

	board = []
	for _ in range(n):
		temp = []
		for _ in range(n):
			q = deque()
			temp.append(q)
		board.append(temp)

	for r,c,m,s,d in fireBalls:
		r -= 1
		c -= 1
		board[r][c].append((m,s,d))		


	for _ in range(k):
		board = moveFireBall(board)
		concatFireBall(board)
		# 맵에 남아있는 fireball 의 질량의합 구하기		

	answer = calMi(board)


	print(answer)

solution()

