# 21608

import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n*n)]

move = [(1,0),(-1,0),(0,1),(0,-1)]
board = [[0]*n for _ in range(n)] # 학샘 넘버가 들어있는 보드
board_empty = [[0]*n for _ in range(n)]
board_dict = {}

for d in data:
	board_dict[d[0]] = d[1:]

def check_empty_board():	
	for i in range(n):
		for j in range(n):
			board_empty[i][j] = 0
			cnt = 0
			for nx,ny in move:
				dx,dy = i+nx,j+ny
				if 0<=dx<n and 0<=dy<n and board[dx][dy] == 0:
					cnt += 1

			board_empty[i][j] += cnt

check_empty_board()

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
# 4 . 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

def find_position(student_infos):
	student_number = student_infos[0]
	friends = student_infos[1:]

	temp_board = [item for row in board for item in row]
	max_value = max(temp_board)

	# board 에 첫번째 사용자 넣을 경우
	if max_value == 0:
		board[1][1] = student_number
		check_empty_board()
		return

	# 1. Board 에서 비어있는 칸 board[i][j] == 0 인데, 주변에 friends 가 있는 칸 
	q_empty = [] # 비어있는 칸
	friends_heap = [] # 비어있는 칸 중 주변에 친구가 있는 칸
	max_friend = 0
	for i in range(n):
		for j in range(n):
			# 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸.
			if board[i][j] == 0:
				empty_temp = board_empty[i][j]
				q_empty.append((empty_temp,i,j))

				friends_cnt = 0
				for nx,ny in move:
					dx,dy = i+nx,j+ny
					if 0<=dx<n and 0<=dy<n and board[dx][dy] in friends:
						friends_cnt += 1

				if friends_cnt > 0:
					max_friend = max(max_friend, friends_cnt)
					heapq.heappush(friends_heap, (friends_cnt*-1,i,j))

			# 여러개라면, 인접한 칸 중 가장 많은 칸

			# 행의 번호가 가장 작은칸, 열의번호가 가장 작은칸

	if friends_heap: # 주변에 친구가 있다면 
		temp = []
		while friends_heap:
			cnt,r,c = heapq.heappop(friends_heap)
			if cnt == max_friend * -1:
				empty_temp = board_empty[r][c]
				temp.append((empty_temp, r, c))
		# temp 배열은 인접한 칸 중 가장 많은 친구가 겹친 칸, 
		# 이중 가장 주변 empty 칸이 많은 칸		
		temp.sort(key=lambda x: (x[0]*-1, x[1], x[2]))
		nextR,nextC = temp[0][1], temp[0][2]				
	else: # 주변에 친구가 없다면, 비어있는칸이 여러개면, 인접한 칸중 가장 많으칸
		q_empty.sort(key=lambda x: (x[0]*-1, x[1], x[2]))
		nextR,nextC = q_empty[0][1], q_empty[0][2]

	board[nextR][nextC] = student_number
	check_empty_board()

def check_pos():
	result = 0
	for i in range(n):
		for j in range(n):
			count = 0
			center = board[i][j]

			for nx,ny in move:
				dx,dy = i+nx,j+ny

				if 0<=dx<n and 0<=dy<n and board[dx][dy] in board_dict[center]:
					count += 1

			if count == 1:
				result += 1
			elif count == 2:
				result += 10
			elif count == 3:
				result += 100
			elif count == 4:
				result += 1000

	return result



def solution():
	for d in data:
		find_position(d)

	answer = check_pos()	

	print(answer)

solution()

