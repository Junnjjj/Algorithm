
moves = [(0,1), (1,0), (0,-1), (-1,0)]
def rotate(k):
    
    dir = 0 # 동 쪽으로 이동부터 시작
    for i in range(len(k) // 2):
        # (0,0) 부터 시작
        dr,dc = i,i
        temp = k[dr][dc]
        check = 0          
        while check != len(k)-1-(2*i):                       
            dr,dc = dr+moves[dir][0],dc+moves[dir][1]
            if dr < 0+i or dc < 0+i or dr >= len(k)-i or dc >= len(k)-i:               
                dr,dc = dr-moves[dir][0],dc-moves[dir][1]
                dir += 1
                if dir == 4:                  
                  temp = k[dr][dc]
                  check += 1
                  dir = 0                  
                continue                          
            temp, k[dr][dc] = k[dr][dc], temp

    for item in k:
      print(item)

def rotate90(arr):
    return list(zip(*arr[::-1]))      

a = [[0, 0, 0], 
     [1, 0, 0], 
     [1, 1, 1]]
a = [[0, 0, 0, 0], 
     [1, 0, 0, 0], 
     [1, 1, 1, 0],
     [1, 1, 1, 0]]
def rotate90(arr):
    return list(zip(*arr[::-1]))

b= rotate90(a)
for z in b:
  print(z)
rotate(a)



# 파이썬
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False;
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if(check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)
                
    return False