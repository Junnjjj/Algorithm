from collections import deque
import sys

input = sys.stdin.readline

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n, m = map(int, input().split())

graph = []
for i in range(n):
	row = list(map(str, input().rstrip()))
	graph.append(row)
	if 'D' in row:
		hole = (i, row.index('D'))
	if 'S' in row:
		start = (i, row.index('S'))

# graph 에서 매분 홍수 영역 증가
def water_flood():
	water = deque()
	for i in range(n):
		for j in range(m):
			if graph[i][j] == '*':
				water.append((i, j))

	while water:
		x, y = water.popleft()
		for nx, ny in move:
			dx, dy = x + nx, y + ny
			if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == '.':
				graph[dx][dy] = '*'


def solution(start):
	q = deque()
	visited = [[False] * m for _ in range(n)]
	min = 0
	q.append((start[0], start[1], min))
	visited[start[0]][start[1]] = True

	while q:
		x, y, now = q.popleft()

		if now == 0 or now == min:
			water_flood()
			min += 1

		for nx, ny in move:
			dx, dy = x + nx, y + ny
			if 0 <= dx < n and 0 <= dy < m and graph[dx][
			    dy] == '.' and not visited[dx][dy]:
				q.append((dx, dy, now + 1))
				visited[dx][dy] = True
			if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 'D':
				return now + 1

	return 'KAKTUS'


ans = solution(start)
print(ans)

# 3 3
# D.*
# ...
# .S.
