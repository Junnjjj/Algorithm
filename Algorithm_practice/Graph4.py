#커리큘럼

from collections import deque
import copy

#N 입력
n = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1) #각 강의 시간 0으로 초기화

#각 간선 종류 입력 받기
for i in range(1, n+1):
  data = list(map(int, input().split()))
  time[i] = data[0] #첫번 째 수는 시간 정보
  for x in data[1:]:
    indegree[i] += 1
    graph[x].append(i)

#위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time) #알고리즘 수행 결과를 담을 리스트
  q = deque()

  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)

  #큐가 빌 때 까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    for i in graph[now]:
      #?
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      #새롭게 진입차수가 0 이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append[i]

  for i in range(1, n+1):
    print(result[i])

topology_sort()