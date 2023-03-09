from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(str,input().rstrip())) for _ in range(r)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

swan = []
water = deque()

for i in range(r):
	for j in range(c):
		if graph[i][j] == 'L':
			swan.append((i,j))
		
		if graph[i][j] == '.':
			water.append((i,j))

			
swan1_x, swan1_y = swan[0]
swan2_x, swan2_y = swan[1]
q = deque()
q.append((swan1_x, swan1_y))
visited = [[False]*c for _ in range(r)]

def melt():
	temp = deque()
	while water:
		x,y = water.popleft()
		for dx,dy in move:
			nx,ny = x+dx,y+dy
			if 0<=nx<r and 0<=ny<c:
				if graph[nx][ny] == 'X':
					graph[nx][ny] = '.'
					temp.append((nx,ny))
					
	return temp

def bfs(q):	
	# 추가된 영역
	temp = deque() 

	global visited

	while q:
		x,y = q.popleft()

		if x == swan2_x and y == swan2_y:
			return True
		
		for dx,dy in move:
			nx,ny = x+dx, y+dy
			if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and (graph[nx][ny] == '.' or graph[nx][ny] == 'L'):
				q.append((nx,ny))
				visited[nx][ny] = True
				temp.append((nx,ny))

	return temp
			
ans = 0
while True:
	check = bfs(q)
	if check == True:		
		print(ans)
		break
	
	water = melt()	
	q = check
	ans += 1

	if len(q) == 0:
		q = deque()
		q.append((swan1_x, swan1_y))
		

# def check_water(graph):
# 	q = deque()
# 	near_land = deque()
# 	visited = [[False] * c for _ in range(r)]
# 	new_graph = [[-1] * c for _ in range(r)]
# 	water = 0

# 	for i in range(r):
# 		for j in range(c):
# 			if graph[i][j] == '.' and not visited[i][j]:
# 				water += 1
# 				q.append((i, j))
# 				visited[i][j] = True
# 				new_graph[i][j] = water

# 				while q:
# 					check = False
# 					x, y = q.popleft()
# 					for dx, dy in move:
# 						nx, ny = x + dx, y + dy
# 						if 0 <= nx < r and 0 <= ny < c:
# 							if graph[nx][ny] == 'X' and not check:
# 								near_land.append((nx, ny))
# 								check = True

# 							if graph[nx][ny] == '.' and not visited[nx][ny]:
# 								q.append((nx, ny))
# 								visited[nx][ny] = True
# 								new_graph[nx][ny] = water

# 	return new_graph, near_land


# def solution():
# 	ans = 0

# 	while True:
# 		near_swan = []
# 		new_graph, near_land_list = check_water(graph)

# 		swan1_x, swan1_y = swan[0]
# 		swan2_x, swan2_y = swan[1]
# 		for dx, dy in move:
# 			nx, ny = swan1_x + dx, swan1_y + dy
# 			if 0 <= nx < r and 0 <= ny < c:
# 				if nx == swan2_x and ny == swan2_y:
# 					return ans

# 				if isinstance(new_graph[nx][ny],
# 				              int) and new_graph[nx][ny] > 0:
# 					near_swan.append(new_graph[nx][ny])

# 		for dx, dy in move:
# 			nx, ny = swan2_x + dx, swan2_y + dy
# 			if 0 <= nx < r and 0 <= ny < c and new_graph[nx][ny] in near_swan:
# 				return ans

# 		for x, y in near_land_list:
# 			graph[x][y] = '.'

# 		ans += 1


# tmp = solution()
# print(tmp)