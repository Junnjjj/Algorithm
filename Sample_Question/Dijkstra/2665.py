import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().rstrip())))
visit = [[0] * n for _ in range(n)]

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        a, x, y = heappop(heap)
        print(x,y)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if room[nx][ny] == 0:
                    heappush(heap, [a + 1, nx, ny])
                else:
                    heappush(heap, [a, nx, ny])

dijkstra()

# 알골스팟 + 다시한번