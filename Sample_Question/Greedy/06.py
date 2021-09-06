import heapq

foodTimes = list(map(int, input().split()))

k = int(input())

def solution(food_times, k):
  n = len(food_times)
  cycle = k // n #첫번째 사이클
  mCycle = cycle
  index = 0
  count = 0

  while True:
    food_times = list(map(lambda x : x-mCycle, food_times)) #food time update

    minus = sum(list(filter(lambda x : x<0, food_times))) #음수 값
    index = (n * cycle) + minus #지나간 음류수
    count = len(list(filter(lambda x : x>0, food_times))) #양수의 개수
    mCycle = (k - index) // count

    cycle += mCycle
    if (k-index) <= count: break
    
  answer = 0   
  for x in range(len(food_times)):
    answer +=1
    if food_times[x] > 0:
      count -= 1
      if count == 0: break
      
  return answer



print(solution(foodTimes, k))