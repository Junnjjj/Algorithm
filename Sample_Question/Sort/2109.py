import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
  data.append(list(map(int, input().split())))

data.sort(reverse=True, key=lambda x : (x[1], x[0]))
first_num = data[0][0]
    
def solution(data, result):

  data.sort(reverse=True, key=lambda x : (x[1], x[0]))
  print(data, result)
  #data[1]의 종류가 1일 때 reulst 에서 최대값더하고 리턴
  d_list = [i[1] for i in data]  
  if len(set(d_list)) == 1:
    result += data[0][0]
    print(result)
    return;

  index = 0
  data_size = len(data) #데이터사이즈
  past_d = data[0][1]


  for i in range(1, data_size):
    
    if data[i][1] == past_d:
      data[i][1] -= 1

      if i+1== data_size or data[i+1][1] != past_d: 
        #재귀호출
        solution(data[i-1:], result)
        break

    else:
      result += data[i][0]
      past_d = data[i][1]
  

solution(data, first_num)

# 9
# 40 3
# 15 3
# 20 1
# 2 1
# 10 3
# 100 2
# 8 2
# 5 20
# 50 10

# 7
# 20 1
# 2 1
# 10 3
# 100 2
# 8 2
# 5 20
# 50 10