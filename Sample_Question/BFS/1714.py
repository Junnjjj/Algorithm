# 1714
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
virus = []
data = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
	for j in range(n):
		if data[i][j] == 2:
			virus.append((i,j))

# 0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간, 불가능할 경우 -1

# 바이러스 m 개를 활성상태로 변환 , 1 <= m <= 10

# 1초 후 상하좌우 복제
# 활성 상태 => 비활성 바이러스로 가면 활성화 됨

move = [(1,0), (-1,0), (0,1), (0,-1)]


def isAllVirus(board):
	for i in range(n):
		for j in range(n):
			if data[i][j] == 1 or data[i][j] == 2: continue # 벽이면 넘어감, 비활성 바이러스인 경우
			if board[i][j] == 1e9: # 하나라도 방문 안했으면 false
				return False				
	return True

def bfs(board, virus_arr):
	q = deque()
	lagest_value = 0
	visited = [[1e9] * n for _ in range(n)]
	for vx,vy in virus_arr:
		q.append((vx,vy,0))
		visited[vx][vy] = 0

	while q:
		x,y,time = q.popleft()

		for nx,ny in move:
			dx,dy = x+nx,y+ny

			if dx < 0 or dx >= n or dy < 0 or dy >= n: continue # 범위 벗어나면
			if board[dx][dy] == 1: continue # 벽이면

			if visited[dx][dy] > time+1:
				q.append((dx,dy,time+1))
				visited[dx][dy] = time+1
				if board[dx][dy] == 2: continue
				lagest_value = max(lagest_value, time+1)

	# 바이러스가 비활성 있을 경우
	return lagest_value, visited


def solution():
	answer = 1e9
	virus_available = list(combinations(virus, m))

	for virus_arr in virus_available:
		time,visited_board = bfs(data, virus_arr)
		if isAllVirus(visited_board):
			answer = min(answer, time)

	return answer if answer != 1e9 else -1

print(solution())