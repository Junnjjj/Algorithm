import sys

MAX_SIZE = 1000000

input = sys.stdin.readline

class Node:
  def __init__(self):
    self.prev = -1
    self.next = -1    


n,m = map(int,input().split())
station = list(map(int,input().split())) 

# node_list = [Node() for _ in range(n)] # 역의 연결 리스트 선언
node_list = [Node() for _ in range(MAX_SIZE+1)] # 1 ~ 1,000,000 => 개 비효율적

for i in range(n):  
  if i == 0:
    node_list[station[0]].prev = station[-1]
    node_list[station[0]].next = station[1]
  elif i == n-1:
    node_list[station[i]].prev = station[i-1]
    node_list[station[i]].next = station[0]
  else:
    node_list[station[i]].prev = station[i-1]
    node_list[station[i]].next = station[i+1]
    


ans = []
work = []
for _ in range(m):    
  cmd = input().rstrip()
  cmd = cmd.split(' ')
  work.append(cmd)

  if cmd[0] == 'BN':
    i,j = int(cmd[1]),int(cmd[2])
    ans.append(node_list[i].next)

    next_node_number = node_list[i].next
    node_list[i].next = j
    
    node_list[j].prev = i
    node_list[j].next = next_node_number

    node_list[next_node_number].prev = j
    
  elif cmd[0] == 'BP':
    i,j = int(cmd[1]),int(cmd[2])
    ans.append(node_list[i].prev)

    prev_node_number = node_list[i].prev
    node_list[i].prev = j
    
    node_list[j].prev = prev_node_number
    node_list[j].next = i

    node_list[prev_node_number].next = j 
  elif cmd[0] == 'CN':
    i = int(cmd[1])
    next_node_number = node_list[i].next # 다음역 폐쇄
    next_next_node_number = node_list[next_node_number].next
    
    ans.append(next_node_number)

    node_list[i].next = next_next_node_number
    node_list[next_next_node_number].prev = i

    
  elif cmd[0] == 'CP':
    i = int(cmd[1])
    prev_node_number = node_list[i].prev # 이전역 폐쇄
    prev_prev_node_number = node_list[prev_node_number].prev

    ans.append(prev_node_number)

    node_list[i].prev = prev_prev_node_number
    node_list[prev_prev_node_number].next = i

for item in ans:
  print(item)
print(ans)


# BN i j : 고유 번호 i를 가진 역의 다음 역의 고유 번호를 출력하고, 그 사이에 고유 번호 j인 역을 설립한다.
# BP i j : 고유 번호 i를 가진 역의 이전 역의 고유 번호를 출력하고, 그 사이에 고유 번호 j인 역을 설립한다.
# CN i : 고유 번호 i를 가진 역의 다음 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
# CP i : 고유 번호 i를 가진 역의 이전 역을 폐쇄하고 그 역의 고유 번호를 출력한다.