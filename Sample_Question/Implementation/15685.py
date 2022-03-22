arr = [[False] * 101 for _ in range(101)]
N = int(input())
direction = [[0, 1], [-1, 0], [0, -1], [1, 0,]]

def rotateFunction(Fixedpoint, Movepoint):
    dx, dy = Fixedpoint[0], Fixedpoint[1]
    mpx, mpy = Movepoint[0], Movepoint[1]
    tx, ty = (-1)*(mpy-dy), 1*(mpx-dx)
    nx, ny = tx+dx, ty+dy
    return (nx, ny)

def dragon_rotate(generation, start, end, list_):
    if generation == 0:
        return
    else:
        new_list = []
        new_list.extend(list_)

        for movepoint in list_:
            x, y = rotateFunction(end, movepoint)
            if 0 <= x <= 100 and 0 <= y <= 100:
                new_list.append([x, y])
                arr[y][x] = True

        new_end = rotateFunction(end, start)
        dragon_rotate(generation-1, start, new_end, new_list)

def findsquare():
    count = 0
    
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
                count += 1

    return count

for _ in range(N):
    x, y, d, g = list(map(int, input().split()))
    nx, ny = x+direction[d][1], y+direction[d][0]
    arr[y][x] = True
    arr[ny][nx] = True
    dragon_rotate(g, [x, y], [nx, ny], [[x, y], [nx, ny]])

count = findsquare()
print(count)