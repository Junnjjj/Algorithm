# 20055

import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
data = list(map(int,input().split()))
q = deque(data)
robot_idxs = []
robot_cnt = 0
robot_exist = [False] * (2*n)

def step1(robot_idxs):
	# 컨베이어 벨트가 로봇과 하나씩 회전	
	end = q.pop()
	q.appendleft(end)
	temp_heap = []
	while robot_idxs:
		rCnt, rIdx = heapq.heappop(robot_idxs)
		robot_exist[rIdx] = False
		rIdx = rIdx + 1

		if rIdx == n-1:
			# 로봇 삭제 이동햇는데 로봇이 내리는 위치라면 즉시 내린다
			pass
		else:
			heapq.heappush(temp_heap, (rCnt, rIdx))
			robot_exist[rIdx] = True
	robot_idxs = temp_heap

	return robot_idxs

def step2(robot_idxs):
	# 가장 벨트에 먼저 올라간 로봇 부터, 회전방향으로 한칸 이동
	# 이동은 내구도 1 이상이며, 로봇이 없어야함
	# 이동할 수 없으면 제자리
	# n 위치에 도달하면 곧바로 내림

	temp_heap = []
	while robot_idxs:
		rCnt, rIdx = heapq.heappop(robot_idxs)
		next_rIdx = rIdx + 1

		if next_rIdx == n-1 and q[next_rIdx] > 0: # 내리는 위치에 도달하면, 로봇 삭제
			q[next_rIdx] -= 1
			robot_exist[rIdx] = False
			continue

		if not robot_exist[next_rIdx] and q[next_rIdx] > 0:			
			heapq.heappush(temp_heap,(rCnt, next_rIdx))
			q[next_rIdx] -= 1
			robot_exist[rIdx] = False
			robot_exist[next_rIdx] = True
		else:
			# 옮길 수 없으면 그대로 있음
			heapq.heappush(temp_heap,(rCnt,rIdx))

	return temp_heap # robot_idxs


def step3(robot_idxs):
	# 0 위치에 로봇 올림	
	global robot_cnt
	if q[0] > 0:
		robot_cnt += 1
		heapq.heappush(robot_idxs,(robot_cnt,0))
		q[0] -= 1
		robot_exist[0] = True

	return robot_idxs

def step4(k):
	# 내구도가 k 개 이상이면 종료, 아니면 1로 돌아감
	count = 0
	for item in q:
		if item == 0:
			count += 1

	if count >= k:
		return True

	return False

def solution():
	cnt = 0	
	robot_idxs = []
	global robot_cnt

	while True:		
		robot_idxs = step1(robot_idxs)		
		robot_idxs = step2(robot_idxs)		
		robot_idxs = step3(robot_idxs)		
		if step4(k):
			print(cnt+1)
			break					
		cnt += 1

solution()