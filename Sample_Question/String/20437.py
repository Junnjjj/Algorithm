from collections import defaultdict

def solution(w,k):  
  string,K = w,k
  len_str = len(string)    
  alpha = defaultdict(list) 
  for i in range(len_str): 
    if string.count(string[i]) >= K: 
      alpha[string[i]].append(i) 
    
  if not alpha: 
    print(-1)
    return 

  min_str,max_str = 1e9, 0
  for idx_lst in alpha.values():
    for j in range(len(idx_lst) - K + 1):
      temp = idx_lst[j+K-1] - idx_lst[j] + 1
      print(temp)

      if temp < min_str: 
        min_str = temp 
      if temp > max_str: 
        max_str = temp

  print(min_str, max_str)  

t = int(input())

for _ in range(t):
  W = str(input().rstrip())
  K = int(input())

  solution(W,K)