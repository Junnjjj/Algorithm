import sys
import heapq
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
  start,end = map(int,input().split())
  heapq.heappush(q,(end, (start,end)))

temp = heapq.heappop(q)
answer = 1
endPoint = temp[0]
while q:  
  temp = heapq.heappop(q)
  if endPoint <= temp[1][0]:
    endPoint = temp[0]
    answer += 1
  
  
print(answer)
