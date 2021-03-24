#상하좌우

#공간의 크기 N
n = int(input())

# n * n x,y의 범위는 1~n
x, y = 1, 1

#여행 계획서
datas = list(input().split())

#L, R, U, D 에 따른 이동방향
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for data in datas:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if data == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  #공간을 벗어날 경우 무시
  if nx <1 or ny <1 or nx >n or ny >n:
    continue
  x,y = nx, ny

print(x, y)