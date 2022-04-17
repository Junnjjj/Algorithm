import sys
from string import ascii_uppercase
from itertools import permutations

input = sys.stdin.readline

k = int(input()) # 사람 수
n = int(input()) # 사다리 높이
people = list(input().rstrip())
ladder = [list(input().rstrip()) for _ in range(n)]
alpha = list(ascii_uppercase)


# 사다리 내려가서 만들어지는 순서
def go():
  arrive = ["x"] * (k-1)
  for p in range(k):

    yLocation = 0
    xLocation = p
    check = False

    while True:
      print(yLocation, xLocation)
      if xLocation > 0 and ladder[yLocation][xLocation-1] == '-': # 왼쪽으로 가는 사다리가 있을 경우        
        xLocation -= 1
      elif xLocation < k-1 and ladder[yLocation][xLocation] == '-': # 오른쪽으로 가는 사다리가 있을 경우
        xLocation += 1

      elif ladder[yLocation][xLocation] == '?': # ? 열에 도착하면 

        for j in (-1,0,1): # 왼쪽 직진 오른쪽 으로 한번 씩 이동
          newYLocation = yLocation          
          idx = xLocation + j
          if idx < 0 or idx >= k-1: # 범위 벗어나면
            continue
          newYLocation += 1
          newXLocation = idx
          while True:
            if newXLocation >0 and ladder[newYLocation][newXLocation] == '-': # 왼쪽이동
              newXLocation -= 1
            elif newXLocation < k-1 and ladder[newYLocation][newXLocation] == '-': # 오른쪽 이동
              newXLocation += 1

            newYLocation += 1

            if newYLocation == n-1: # 끝에 도달하면
              if alpha[p] == people[newXLocation]: # 같으면
                if j == -1: # 왼쪽 이동일 때
                  arrive[k-1] = '-'                  
                elif j == 1: # 오른쪽 이동일 때
                  arrive[k+1] = '-'

                check = True                
              break
          if check: # 맞는 조건을 찾았으므로 나머지 (왼쪽 직진 오른쪽) 안해도됨
            break
            
      yLocation += 1


  return arrive

ans = go()
print(ans)



# def go():
#   arrive = ["x"] * k
#   for p in range(k):

#     yLocation = 0
#     xLocation = p

#     while True:
#       if xLocation > 0 and ladder[yLocation][xLocation-1] == '-': # 왼쪽으로 가는 사다리가 있을 경우        
#         xLocation -= 1
#       elif xLocation < k-1 and ladder[yLocation][xLocation] == '-': # 오른쪽으로 가는 사다리가 있을 경우
#         xLocation += 1

#       yLocation += 1

#       if yLocation == n-1:
#         break

#     arrive[xLocation] = alpha[p]

#   return arrive


# go()
# print(ans)

# 4
# 3
# BCDA
# *--
# -*-
# --*    

# 10
# 5
# ACGBEDJFIH
# *-***-***
# -*-******
# **-*-***-
# -**-***-*
# **-*-*-*-