# 구현 문제
import sys
from collections import Counter
input = sys.stdin.readline

u,n = map(int,input().split()) # u 금액의 상한선, n 경매에 참여한 횟수

bid = []
money = []
minMoney = 1e9
for _ in range(n):
  s,p = map(str,input().split())
  bid.append((s, int(p)))
  money.append(int(p))
  minMoney = min(minMoney, int(p))

temp = Counter(money)

anotherMin = 1e9
check = False
for k,v in temp.items():
  if v == 1:
    check = True
    anotherMin = min(anotherMin, k)

  
a = temp.most_common()
# print('a', a[::-1])

# Check False 이면 전부 2 이상 => 가장 적은 수의 사람이 제시한 가격
if not check:      
  minValue = a[-1] # (7,1)
  reverseA = a[::-1]
  mini = minValue[0]
  for idx in range(1,len(a)):
    k,v = reverseA[idx]
    if v == minValue[1]:
      mini = min(k,mini)
    else:
      break  
  for item in bid:
    if item[1] == mini:
      print(*item)
      exit()
# Check True 이면 1 인게 존재      
else:
  for item in bid:
    if item[1] == anotherMin:
      print(*item)
      exit()  

# 10 6
# Lew 10
# HONG 10
# CD 5
# Fe 5
# CN 7
# CD 7



# 우선 가장 적은 수의 사람이 제시한 가격을 찾는다. 
# 이러한 경우가 여럿 있다면, 가장 낮은 가격으로 물건을 팔게 된다. 
# 이때, 그 가격을 제시한 사람들 중에서 가장 먼저 제시한 사람이 물건을 살 수 있게 된다.