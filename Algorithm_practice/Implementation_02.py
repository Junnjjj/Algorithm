#왕실 나이트
#8 * 8 좌표 평면
#나이트의 이동방향 L

# move_types = ['RRU', 'RRD', 'DDR', 'DDL', 'LLU', 'LLD', 'UUR', 'UUL']
move_types = [(2,1),(2,-1),(1,-2),(-1,-2),(-2,1),(-2,-1),(1,2),(-1,2)]


#현재 나이트 위치(a1)
place = input()
row = int(place[1])
column = int(ord(place[0])) - int(ord('a')) + 1

print(row, column)

count = 0
for i in move_types:
  next_row = row + i[0]
  next_column = column + i[1]
  if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <=8:
    count += 1

print(count)

