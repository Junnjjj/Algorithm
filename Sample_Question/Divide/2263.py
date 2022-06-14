#Devide and Conquer
import sys
input = sys.stdin.readline

def solve(IL,IR, PL, PR, root): # InOrder left,right / PostOrder left,right root
  # Left Right 로 나눠야함
  Iroot = inOrder.index(root): # 인오더에서 루트 위치
  IleftSize = Iroot-1
  IrightSize = len(inOrder)


  
n = int(input())
inOrder = list(map(int,input().split()))
postOrder = list(map(int,input().split()))


root = postOrder[-1]