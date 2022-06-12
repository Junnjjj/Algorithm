import sys
input = sys.stdin.readline

# 20437 문자열 게임
from collections import defaultdict

def solution(w,k):  
  string,K = w,k
  len_str = len(string)    
  alpha = defaultdict(list) 
  for i in range(len_str): 
    if string.count(string[i]) >= K: 
      # K개 이상인 문자의 인덱스 딕셔너리 저장
      alpha[string[i]].append(i) 

  # 딕셔너리에 저장되는게 없다면 -1 출력  
  if not alpha: 
    print(-1)
    return 

  min_str,max_str = 1e9, 0
  for idx_lst in alpha.values():
    for j in range(len(idx_lst) - K + 1):
      temp = idx_lst[j+K-1] - idx_lst[j] + 1

      if temp < min_str: 
        min_str = temp 
      if temp > max_str: 
        max_str = temp

  print(min_str, max_str)  

# 16234 인구이동
