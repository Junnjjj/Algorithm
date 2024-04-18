# 14890 implemention
import sys
from collections import deque
input = sys.stdin.readline

n,l = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

# 오른쪽, 아래
move = [(0,1),(1,0)]

def checkStick(line):

	# 무조건 i 일 떄 높을경우 가정
	bridge = [False] * n
	for i in range(n):
		# 왼쪽확인
		if i-1 >= 0:
			if line[i] - line[i-1] > 1: return False
			if line[i] - line[i-1] == 1:
				# l 만큼 왼쪽으로 가고
				for k in range(l):
					di = i + (k+1)*-1
					if di < 0 or line[i] - line[di] != 1: return False
					if bridge[di]: return False # 이미 다리가 있는 경우

				# 전부 통과하면, bridge True 해줌
				for k in range(l):
					di = i + (k+1)*-1
					bridge[di] = True


		# 오른쪽확인
		if i+1 < n:
			if line[i] - line[i+1] > 1: return False
			if line[i] - line[i+1] == 1:
				for k in range(l):
					di = i + (k+1)
					if di >= n or line[i] - line[di] != 1: return False
					if bridge[di]: return False

				for k in range(l):
					di = i + (k+1)
					bridge[di] = True

	return True

def makeLineList(i,j,dir):
	line = []
	for k in range(n):
		nx,ny = move[dir][0]*k, move[dir][1]*k
		dx,dy = i+nx, j+ny
		line.append(data[dx][dy])

	return line

def solution():
	ans = 0

	for i in range(n):
		for j in range(n):
			if i == 0: # 아래로 이동
				line = makeLineList(i,j,1)
				if checkStick(line):
					ans += 1

			if j == 0:
				line =makeLineList(i,j,0)
				if checkStick(line):
					ans += 1


	print(ans)

solution()