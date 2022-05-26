import sys

input = sys.stdin.readline
 
string = list(input().rstrip())
result = ['']*len(string)
 
 
def solution(arr, start):
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[start+idx] = _min    
    print("".join(result))
    solution(arr[idx+1:], start+idx+1)
    solution(arr[:idx], start)
 
solution(string, 0)

# 중앙 뽑으면 오른쪽 정렬 순으로 출력

# ZOAC
# 2
# arr[:2]
# arr[2:]

# A
# AI
# AIK
# AINK
# ALINK
# ARLINK
# ARTLINK
# SARTLINK
# STARTLINK

# A
# AI
# AIK
# ALIK
# ALINK
# ARLINK
# ARTLINK
# SARTLINK
# STARTLINK