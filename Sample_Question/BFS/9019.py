import sys
from collections import deque

input = sys.stdin.readline
MAX = 10000

class command:
  def __init__(self,N,B):
    self.N = N
    self.B = B
    
  def make_four(self):
    # 자리수 판단 1 => 0001, 10 => 0010, 110 => 0110
    str_n = str(self.N)
    length = len(str_n)
    zero_length = 4-length
    zero = f"{'':0>{zero_length}}"
    str_n = zero + str_n
    self.N = str_n

  def command_d(self):
    n = int(self.N)
    n = (2*n)//10000 if 2*n >= MAX else 2*n
    self.make_four()
    return n

  def command_s(self):
    n = int(self.N)
    n = n-1 if n-1 != 0 else 9999
    self.make_four()
    return str(n)

  def command_l(self):
    self.make_four()
    n = self.N
    n = n[1]+n[2]+n[3]+n[0]
    return n

  def command_r(self):
    self.make_four()
    n = self.N
    n = n[3]+n[0]+n[1]+n[2]
    return n

  def run_all_functions(self):
    result = []
    function_list = [self.command_d, self.command_s, self.command_l, self.command_r]

    for func in function_list:
        result.append(func())

    return result

 
def bfs(a,b):
  q = deque()
  visited = ['X'] * (1+MAX)

  q.append(a)
  visited[a] = 'A'

  while q:
    prev = q.popleft()
    register_command = command(prev,b)

    next_list = register_command.run_all_functions()
    print(next_list)
      
  

t = int(input())
for _ in range(t):
  a,b = map(int,input().split())
  bfs(a,b)