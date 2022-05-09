from collections import deque

def shift(arr):
    q = deque(arr)
    tmp = q.pop()
    q.appendleft(tmp)
    return list(q)

move = [(1,0),(0,1),(-1,0),(0,-1)]
def rotate(arr):
    size = len(arr)

    row_size = len(arr)
    col_size = len(arr[0])
  
    dr,dc = 0,0
    rotate_way = 0
    while True:     
        nr,nc = dr+move[rotate_way][0], dc+move[rotate_way][1]        
        if nr == 0 and nc == 0:
            break
        if nr < 0 or nc <0 or nr >= row_size or nc >= col_size:
            rotate_way += 1
            continue
        arr[nr][nc], arr[dr][dc] = arr[dr][dc], arr[nr][nc]
        dr,dc = nr,nc

    return arr

def solution(rc, operations):
    for o in operations:
        if o == "Rotate":
            rc = rotate(rc)
        else:
            rc = shift(rc)
        
    answer = rc
    return answer

r = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
r = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12]]
print(rotate(r))

# op = ["Rotate", "ShiftRow"]
# solution(r,op)