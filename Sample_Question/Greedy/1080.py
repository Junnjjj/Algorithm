import sys
input = sys.stdin.readline

def change(arr, r,c):  
  for i in range(3):
    for j in range(3):      
      arr[r+i][c+j] = 1 if arr[r+i][c+j] == 0 else 0
  
n,m = map(int,input().split())
A = [list(map(int,input().rstrip())) for _ in range(n)]
B = [list(map(int,input().rstrip())) for _ in range(n)]

answer =  0
for i in range(n-3+1):
  for j in range(m-3+1):
    if A[i][j] != B[i][j]:
      change(A, i,j)
      answer += 1

if A != B:
  print(-1)
else:
  print(answer)

    

 # 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다