import sys
from collections import deque

input = sys.stdin.readline

def solution(arr, idx):

  s1,s2,s3 = list(arr[0]),list(arr[1]),list(arr[2])
  visited = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
  
  i = 0
  q = deque([(0,0)])
  visited[0][0] = True
  
  while q:    
    for _ in range(len(q)):
      a,b, = q.popleft()
      if a < len(s1) and s1[a] == s3[i] and not visited[a+1][b]:
        q.append((a+1, b))
        visited[a+1][b] = True
      if b < len(s2) and s2[b] == s3[i] and not visited[a][b+1]:
        q.append((a, b+1))
        visited[a][b+1] = True

    i += 1
    
  tf = 'yes' if i == len(s3)+1 else 'no'
  print('Data set {0}: {1}'.format(idx+1, tf))  
  

t = int(input())

for i in range(t):
  words = list(map(str,input().split()))

  solution(words,i)
