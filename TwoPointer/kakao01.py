import heapq
from collections import Counter

def twoPointer(arr,M):
    start,end = 0,1
    length = 0
    gem_dict = Counter(arr[start:end])    
    q = []
    
    while end < len(arr) and start < end:
        print(start,end)
               
        if len(gem_dict) == M:
            heapq.heappush(q,(end-start, [start+1,end+1]))
          
            gem_dict[arr[start]] -=1
            if gem_dict[arr[start]] == 0:
              del gem_dict[arr[start]]
            start +=1            
            
        else:
            
            end +=1
                 
            if end >= len(arr):
                break               
            if arr[end] not in gem_dict:
                gem_dict[arr[end]] = 1
            else:
                gem_dict[arr[end]] += 1
            
    return heapq.heappop(q)

def solution(gems):
    answer = []
    type_size = len(set(gems))
    
    answer = twoPointer(gems,type_size)
    
    return answer[1]

g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g = ["AA", "AB", "AC", "AA", "AC"]
a = solution(g)
print(a)