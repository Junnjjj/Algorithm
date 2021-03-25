  #게임 개발
#맵의 크기는 N x M 직사각형, 각 각의 칸은 육지 혹은 바다
#캐릭터는 동서남북 하나로 바라본다

#맵의 각칸은 (A,B), A는 북쪽으로 떨어진 칸의 개수, B는 서쪽으로 떨어진 칸 개수


#맵의 크기
n, m =map(int, input().split())

#방문한 위치를 저장하기 위한 맵 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

#플레이어 위치, 방향
x, y, direction = map(int, input().split())
#현재 방문한 위치 처리
d[x][y] = 1


#맵 특징 입력
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

#북, 동, 남 ,서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

#시뮬레이션 실행
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  #회전한 이후 가보지 않은 칸 일 경우 , 육지일 경우(0) 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time +=1
  #4방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    #뒤로 갈 수 있다면 이동
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #뒤가 바다로 막혀있을 때
    else:
      break
    turn_time = 0

print(count)



