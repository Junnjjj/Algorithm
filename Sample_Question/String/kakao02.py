#메뉴 리뉴얼

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        combinationArray=[]
        for order in orders:
            combinationArray+=list(combinations(sorted(order),c))
        combinationArray=Counter(combinationArray)
        print("c=",c,combinationArray) # 이해하시는데 도움이 되실겁니다.
        answer+=[''.join(k) for k, v in combinationArray.items() if v == max(combinationArray.values()) and v>1]
    
    return sorted(answer)

a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b = [2,3,4]
print(solution(a,b))