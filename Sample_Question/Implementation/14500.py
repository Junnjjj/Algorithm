import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]

threeHorizonMove = [(-1,0),(1,0),(0,-1),(-1,1),(1,1),(-1,2),(1,2),(0,3)]
threeVerticalMove = [(0,-1),(-1,0),(0,1),(1,-1),(1,1),(2,-1),(3,0),(2,1)]

twoHorizonMove = [[(-1,0), (1,1)], [(1,0),(-1,1)], [(1,0),(1,1)]] # 2*2 도 포함
twoVerticalMovew = [[(0,-1),(1,1)],[(0,1),(1,-1)]]

result = 0
for y in range(n):
  for x in range(m):

    # 2칸일 경우(수평)
    if x+1 < m:
      TwoSum = map[y][x] + map[y][x+1]
      maxRemain = 0
      for remain in twoHorizonMove:
        ny1,nx1, ny2,nx2 = y+remain[0][0],x+remain[0][1], y+remain[1][0],x+remain[1][1]
        if 0 <= ny1 < n and 0 <= nx1 < m and 0 <= ny2 < n and 0 <= nx2 < m:
          maxRemain = max(maxRemain, (map[ny1][nx1] + map[ny2][nx2]))
      TwoSum = maxRemain + TwoSum      

    # 수직
    if y+1 < n:
      TwoSumH = map[y][x] + map[y+1][x]
      maxRemain = 0
      for remain in twoVerticalMovew:
        ny1,nx1, ny2,nx2 = y+remain[0][0],x+remain[0][1], y+remain[1][0],x+remain[1][1]
        if 0 <= ny1 < n and 0 <= nx1 < m and 0 <= ny2 < n and 0 <= nx2 < m:
          maxRemain = max(maxRemain, (map[ny1][nx1] + map[ny2][nx2]))
      TwoSumH = maxRemain + TwoSumH

    # 3칸일 경우(수평)
    if x+2 < m:
      ThreeSum = map[y][x] + map[y][x+1] + map[y][x+2]
      maxRemain = 0
      for remain in threeHorizonMove:
        ny, nx = y+remain[0], x+remain[1]
        if 0 <= ny < n and 0 <= nx < m:
          maxRemain = max(maxRemain, map[ny][nx])
      ThreeSum = maxRemain + ThreeSum

    # 3칸일 경우(수직)
    if y+2 < n:
      ThreeSumH = map[y][x] + map[y+1][x] + map[y+2][x]
      maxRemain = 0
      for remain in threeVerticalMove:
        ny, nx = y+remain[0], x+remain[1]
        if 0 <= ny < n and 0 <= nx < m:
          maxRemain = max(maxRemain, map[ny][nx])
      ThreeSumH = maxRemain + ThreeSumH

    result = max(result, TwoSum, ThreeSum, TwoSumH, ThreeSumH)    

print(result)
