# 16235 

import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
a = []
trees = []
for _ in range(n):	
	a.append(list(map(int,input().split())))
for _ in range(m):
	x,y,z = map(int,input().split())
	trees.append((x-1,y-1,z))

# a 는 각 칸에 추가되는 양분의 양, z 는 나이
board = [[5]* n for _ in range(n)] # 처음 양분은 5

def spring(tree_board):
	# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
	# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
	# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
	# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

	for i in range(n):
		for j in range(n):
			if not tree_board[i][j]: continue

			q = deque()
			deadTree = 0

			while tree_board[i][j]:
				age = tree_board[i][j].popleft()
				if board[i][j] >= age: # 양분이 나이보다 많으면, 자신의 나이만큼 양분 먹고, 나이 + 1
					q.append(age+1)
					board[i][j] -= age
				else: # 양분이 부족해 먹을 수 없으면, 나무는 죽음
					deadTree += age//2

			# 새로운 나무목록			
			tree_board[i][j] = q
			if deadTree > 0:
				dead_tree_board[i][j] += deadTree

def summer():
	# 죽은 나무가 양분으로 변한다.
	for i in range(n):
		for j in range(n):
			if dead_tree_board[i][j] > 0:
				board[i][j] += dead_tree_board[i][j]
				dead_tree_board[i][j] = 0


def autumn(tree_board):
	# 나무가 번식, 번식하는 나무는 5의 배수, 인접 8개 칸에 1 인 나무 생김
	move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
	for i in range(n):
		for j in range(n):
			if not tree_board[i][j]: continue

			q = deque()

			while tree_board[i][j]:
				age = tree_board[i][j].popleft()
				q.append(age)
				if age % 5 == 0:
					for nx,ny in move:
						dx,dy = i+nx,j+ny
						if 0<=dx<n and 0<=dy<n:							
							tree_board[dx][dy].appendleft(1)

			tree_board[i][j] = q


def winter():
	# 로봇이 돌아다니면서 양분심음 a ..
	for i in range(n):
		for j in range(n):
			board[i][j] += a[i][j]	

dead_tree_board = [[0] * n for _ in range(n)]
def solution():
	ans = 0
	# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
	q = deque()
	tree_board = []
	for _ in range(n):
		temp = []
		for _ in range(n):
			temp.append(deque())
		tree_board.append(temp)

	trees.sort(key=lambda x:x[2]) # 어린 나무부터 양분윽 먹기 때문에 	
	for r,c,z in trees:	
		tree_board[r][c].append(z)				

	for _ in range(k):
		spring(tree_board)

		summer()

		autumn(tree_board)

		winter()			

	for row in tree_board:		
		for item in row:
			ans += len(item)		

	return ans

print(solution())