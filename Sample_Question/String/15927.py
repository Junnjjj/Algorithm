# import sys
# from collections import deque

# input = sys.stdin.readline

# word = list(input().rstrip())

# # PALINDROME
# def findPalidrome(w):
#   size = len(w)  
#   for i in range(0, size//2):    
#     if w[i] != w[size-i-1]:
#       return False # 회문이 아니다
    
#   return True

# result = 0
# wordSize = len(word)
# for i in range(wordSize):  
#   for j in range(i, wordSize+1):
#     checkWord = word[i:j]
    
#     if not findPalidrome(checkWord):            
#       result = max(result, len(checkWord))

# print(result if result != 0 else -1)


import sys
inmput = sys.stdin.readline


def check(a,left,right):
    while left < right:
        if a[left] != a[right]:
            return 0
        left += 1
        right -= 1
    return 1


s = input().rstrip()
n = len(s)
# 최대 길이가 회문 아니면 n
if not check(s,0,n-1):
    print(n)
# 최대길이에서 하나뺀게 회문 아니면 n-1
elif not check(s,0,n-2):
    print(n-1)
else:
    print(-1)